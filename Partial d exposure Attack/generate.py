from Crypto.Util.number import *
from sage.all import *

nbit = 1024
p = getPrime(nbit)
q = getPrime(nbit)
e = 65537
n = p * q
assert p + q < int(3 * N(sqrt(n)))
d = pow(e, -1, (p - 1) * (q - 1))
m = bytes_to_long(open("flag.txt", "rb").read())
c = pow(m, e, n)
leak = d & (2**600 - 1)
with open("9/output.txt", "w") as f:
    f.write(f"{n = }\n{e = }\n{c = }\n{leak = }\n")