# Pollard's p-1 Method

from gmpy2 import fac
from Crypto.Util.number import *

with open("13/output.txt", "r") as f:
    n = int(f.readline().split(" = ")[1])
    e = int(f.readline().split(" = ")[1])
    c = int(f.readline().split(" = ")[1])

a = 2
B = 65535
while True:
    b = fac(B)
    tmp2 = pow(a, b, n) - 1
    gcd_value = GCD(tmp2, n)
    if gcd_value == 1:
        B += 1
    elif gcd_value == n:
        B -= 1
    else:
        p = gcd_value
        q = n // p
        assert p * q == n
        d = pow(e, -1, (p - 1) * (q - 1))
        m = pow(c, d, n)
        print((long_to_bytes(m)).decode())
        break