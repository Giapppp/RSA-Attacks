#Common modulus attack
from sage.all import *
from Crypto.Util.number import *

def attack(C1, C2, e1, e2, N):
    _, x, y = xgcd(e1, e2)
    m = (pow(C1, x, N) * pow(C2, y, N)) % N
    return m

#Test
p = getPrime(1024)
q = getPrime(1024)
N = p * q
e1 = getPrime(512)
e2 = getPrime(512)
m = int.from_bytes(open("../flag.txt", "rb").read(), "big")
C1 = pow(m, e1, N)
C2 = pow(m, e2, N)
dec = attack(C1, C2, e1, e2, N)
print(long_to_bytes(dec))
