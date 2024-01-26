# Small e attack
from Crypto.Util.number import *
from gmpy2 import iroot

def attack(c:int, e:int) -> int:
    return int(iroot(c, e)[0])

#Test
p = getPrime(1024)
q = getPrime(1024)
n = p * q
e = 3
m = int.from_bytes(open("../flag.txt", "rb").read(), "big")
c = pow(m, e, n)
assert pow(m, e) == c
dec = attack(c, e)
print(dec.to_bytes((dec.bit_length() + 7) // 8, "big"))