#  Franklin-Reiter Related Message Attack
from Crypto.Util.Padding import pad
from Crypto.Util.number import *
from sage.all import *

with open("6/output.txt", "r") as f:
    n = int(f.readline().split(" = ")[1])
    e = int(f.readline().split(" = ")[1])
    c1 = int(f.readline().split(" = ")[1])
    c2 = int(f.readline().split(" = ")[1])

#Greatest Common Divisor of two polynomials
pgcd = lambda g1, g2: g1.monic() if not g2 else pgcd(g2, g1%g2)

x = PolynomialRing(Zmod(n), 'x').gen()
f1 = x**e - c1
#We know that length of the message is 17 and message using pkcs7 to padding, so it will have 15 bytes b"\x0f" at the end
f2 = (2**(15*8) * x + bytes_to_long(b"\x0f" * 15))**e - c2

g = int(-pgcd(f1, f2)[0])
print(long_to_bytes(g))