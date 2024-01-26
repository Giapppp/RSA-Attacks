

# This file was *autogenerated* from the file 8/8.sage
from sage.all_cmdline import *   # import sage library

_sage_const_1 = Integer(1); _sage_const_1p0 = RealNumber('1.0'); _sage_const_2 = Integer(2); _sage_const_7 = Integer(7); _sage_const_0 = Integer(0); _sage_const_1024 = Integer(1024); _sage_const_0p5 = RealNumber('0.5')# Partial p exposure attack
from sage.all import *
from Crypto.Util.number import *

with open("8/output.txt", "r") as f:
    n = Integer(int(f.readline().split(" = ")[_sage_const_1 ]))
    e = Integer(int(f.readline().split(" = ")[_sage_const_1 ]))
    c = Integer(int(f.readline().split(" = ")[_sage_const_1 ]))
    leak = Integer(int(f.readline().split(" = ")[_sage_const_1 ]))

def small_roots(f, X, beta=_sage_const_1p0 , m=None):
    N = f.parent().characteristic()
    delta = f.degree()
    if m is None:
        epsilon = RR(beta**_sage_const_2 /f.degree() - log(_sage_const_2 *X, N))
        m = max(beta**_sage_const_2 /(delta * epsilon), _sage_const_7 *beta/delta).ceil()
    t = int((delta*m*(_sage_const_1 /beta - _sage_const_1 )).floor())
    
    f = f.monic().change_ring(ZZ)
    P,(x,) = f.parent().objgens()
    g  = [x**j * N**(m-i) * f**i for i in range(m) for j in range(delta)]
    g.extend([x**i * f**m for i in range(t)]) 
    B = Matrix(ZZ, len(g), delta*m + max(delta,t))

    for i in range(B.nrows()):
        for j in range(g[i].degree()+_sage_const_1 ):
            B[i,j] = g[i][j]*X**j

    B =  B.LLL()
    f = sum([ZZ(B[_sage_const_0 ,i]//X**i)*x**i for i in range(B.ncols())])
    roots = set([f.base_ring()(r) for r,m in f.roots() if abs(r) <= X])
    return [root for root in roots if N.gcd(ZZ(f(root))) >= N**beta]

t = (int(leak)).bit_length()
x = PolynomialRing(Zmod(n), 'x').gen()
f = leak * _sage_const_2 **(_sage_const_1024  - t) + x
lsb = small_roots(f, X = _sage_const_2 **(_sage_const_1024  - t), beta = _sage_const_0p5 )
p = int(f(lsb))
q = n // p
assert p * q == n
phi = (p - _sage_const_1 ) * (q - _sage_const_1 )
d = pow(e, -_sage_const_1 , phi)
m = pow(c, d, n)
print((long_to_bytes(m)).decode())

