from Crypto.Util.Padding import pad
from Crypto.Util.number import *

m = open("flag.txt", "rb").read()
m_pad = pad(m, 16)
print(m_pad)
p = getPrime(1024)
q = getPrime(1024)
n = p * q
e = 3
c1 = pow(bytes_to_long(m), e, n)
c2 = pow(bytes_to_long(m_pad), e, n)
with open("6/output.txt", "w") as f:
    f.write(f"{n = }\n{e = }\n{c1 = }\n{c2 = }\n")