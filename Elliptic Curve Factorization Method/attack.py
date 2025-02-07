# Elliptic Curve Factorization Method
# Resource: "Rational Points on Elliptic Curves" by Joseph H. Silverman and John Tate, page 149
from sage.all import *
import re

def ecm(n, d_max):
    while True:
        assert gcd(n, 6) == 1, "Use another method"
        assert Integer(n).is_perfect_power() is False, "Use another method"
        while True:
            b, x1, y1 = [randint(1, n) for _ in range(3)]
            c = (y1**2 - x1**3 - b * x1) % n
            if gcd(4 * b**3 + 27 * c**2, n) == 1:
                break
        E = EllipticCurve(Zmod(n), [b, c])
        P = E(x1, y1)
        Q = P
        for i in range(2, d_max):
            try:
                Q = i*P
                P = Q
            except ZeroDivisionError as e:
                vs = list(map(ZZ, re.findall('[0-9]+', e.args[0])))
                f = gcd(vs[0], n)
                if f > 1 and f < n:
                    return [f, n//f]

#Test
from Crypto.Util.number import *

p = getPrime(32)
q = getPrime(32)
n = p * q
d_max = 32
print(ecm(n, d_max))

