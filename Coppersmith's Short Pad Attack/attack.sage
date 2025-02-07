#Coppersmith's Short Pad 
from sage.all import *
from Crypto.Util.number import *

with open("7/output.txt", "r") as f:
    n = Integer(int(f.readline().split(" = ")[1]))
    e = Integer(int(f.readline().split(" = ")[1]))
    c1 = Integer(int(f.readline().split(" = ")[1]))
    c2 = Integer(int(f.readline().split(" = ")[1]))

pgcd = lambda g1, g2: g1.monic() if not g2 else pgcd(g2, g1%g2)

def attack(n, e, c1, c2):
    PRxy.<x,y> = PolynomialRing(Zmod(n))
    PRx.<xn> = PolynomialRing(Zmod(n))
    PRZZ.<xz,yz> = PolynomialRing(Zmod(n))

    g1 = x^e - c1
    g2 = (x+y)^e - c2

    q1 = g1.change_ring(PRZZ)
    q2 = g2.change_ring(PRZZ)

    h = q2.resultant(q1)
    h = h.univariate_polynomial()
    h = h.change_ring(PRx).subs(y=xn)
    h = h.monic()

    kbits = n.nbits()//(2*e*e)
    diff = h.small_roots(X=2^kbits, beta=0.5)[0]  # find root < 2^kbits with factor >= n^0.5

    m = PolynomialRing(Zmod(n), 'm').gen()
    f1 = m^e - c1
    f2 = (m + diff)^e - c2
    m = int(-pgcd(f1, f2)[0])
    return m

m = attack(n, e, c1, c2)
print(long_to_bytes(int(m)))

