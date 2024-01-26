#Stereotyped Message attack

from Crypto.Util.number import *
from sage.all import *

with open("19/output.txt", "r") as f:
    n = Integer(int(f.readline().split(" = ")[1]))
    e = Integer(int(f.readline().split(" = ")[1]))
    c = Integer(int(f.readline().split(" = ")[1]))

known = b"Merry Christmas and Happy New Year! I won't talk to you that the flag is: "
known_int = bytes_to_long(known)

x = PolynomialRing(Zmod(n), 'x').gen()
f = (known_int * 2**(17 * 8) + x)**e - c
ans = f.small_roots(X = 2**(17 * 8), beta = 0.5)[0]
print(long_to_bytes(int(ans)).decode())