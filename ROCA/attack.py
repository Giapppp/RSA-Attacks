# Return Of Coppersmith's Attack

from Crypto.Util.number import *
from roca_attack import roca

with open("17/output.txt", "r") as f:
    n = int(f.readline().split(" = ")[1])
    e = int(f.readline().split(" = ")[1])
    c = int(f.readline().split(" = ")[1])

p, q = roca(n)
d = pow(e, -1, (p - 1) * (q - 1))
m = pow(c, d, n)
print(long_to_bytes(m).decode())