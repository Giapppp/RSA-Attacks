# Boneh-Duffee Attack

from Crypto.Util.number import *
from sage.all import *
import itertools

with open("12/output.txt", "r") as f:
    n = Integer(int(f.readline().split(" = ")[1]))
    e = Integer(int(f.readline().split(" = ")[1]))
    c = Integer(int(f.readline().split(" = ")[1]))

#From https://github.com/defund/coppersmith/blob/master/coppersmith.sage
def small_roots(f, bounds, m=1, d=None):
	if not d:
		d = f.degree()

	R = f.base_ring()
	N = R.cardinality()
	
	f /= f.coefficients().pop(0)
	f = f.change_ring(ZZ)

	G = Sequence([], f.parent())
	for i in range(m+1):
		base = N^(m-i) * f^i
		for shifts in itertools.product(range(d), repeat=f.nvariables()):
			g = base * prod(map(power, f.variables(), shifts))
			G.append(g)

	B, monomials = G.coefficient_matrix()
	monomials = vector(monomials)

	factors = [monomial(*bounds) for monomial in monomials]
	for i, factor in enumerate(factors):
		B.rescale_col(i, factor)

	B = B.dense_matrix().LLL()

	B = B.change_ring(QQ)
	for i, factor in enumerate(factors):
		B.rescale_col(i, 1/factor)

	H = Sequence([], f.parent().change_ring(QQ))
	for h in filter(None, B*monomials):
		H.append(h)
		I = H.ideal()
		if I.dimension() == -1:
			H.pop()
		elif I.dimension() == 0:
			roots = []
			for root in I.variety(ring=ZZ):
				root = tuple(R(root[var]) for var in f.variables())
				roots.append(root)
			return roots

	return []

k, s = PolynomialRing(Zmod(e), 'k,s').gens()
f = 2*k*((n+1)//2 - s) + 1
k,s = small_roots(f, bounds = (floor(pow(n, 0.25)), 2**1024), m=3, d=4)[0]
p,q = var('p q')
p,q = [int(i.right_hand_side()) for i in solve([p*q == n, (p+q) / 2 == int(s)], p,q)[0]]

d = pow(e, -1, (p - 1) * (q - 1))
print(long_to_bytes(pow(c, d, n)).decode())