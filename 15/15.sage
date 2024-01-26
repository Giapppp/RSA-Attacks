# Factoring with Cyclotomic Polynomials

from Crypto.Util.number import *
from sage.all import *

with open("15/output.txt", "r") as f:
    n = Integer(int(f.readline().split(" = ")[1]))
    e = Integer(int(f.readline().split(" = ")[1]))
    c = Integer(int(f.readline().split(" = ")[1]))

k = 3

R = Zmod(n)["x"]
while True:
    Q = R.quo(R.random_element(k))
    pp = gcd(ZZ(list(Q.random_element() ^ n)[1]), n)
    if pp != 1:
        qq = sum([pp**i for i in range(k)])
        rr = n // (pp * qq)
        assert n == pp * qq * rr
        break
phi = (pp - 1) * (qq - 1) * (rr - 1)
d = pow(e, -1, phi)
m = pow(c, d, n)
print(long_to_bytes(m))