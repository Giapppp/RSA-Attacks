#Hastad's Broadcast Attack
from sage.all import *
from Crypto.Util.number import *
from gmpy2 import iroot

e = 17
Cs = []
Ns = []

with open("5/output.txt", "r") as f:
    for _ in range(e):
        e = int(f.readline().split(" = ")[1])
        Ns.append(int(f.readline().split(" = ")[1]))
        Cs.append(int(f.readline().split(" = ")[1]))

m_e = crt(Cs, Ns)
m = m_e.nth_root(e)
print(long_to_bytes(int(m)))