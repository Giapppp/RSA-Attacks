from Crypto.Util.number import *
import os

#Padding message with random bytes
def random_padding(m:bytes) -> bytes:
    pad_length = 16 - len(m)%16
    return m + os.urandom(pad_length)

m = open("flag.txt", "rb").read() * 5
e = 3
p = getPrime(1024)
q = getPrime(1024)
n = p * q

M = [random_padding(m) for _ in range(2)]
C = [pow(bytes_to_long(m), e, n) for m in M]

with open("7/output.txt", "w") as f:
    f.write(f"{n = }\n{e = }\n{C[0] = }\n{C[1] = }\n")
