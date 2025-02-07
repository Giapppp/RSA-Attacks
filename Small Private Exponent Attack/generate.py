from Crypto.Util.number import *

p = getPrime(1024)
q = getPrime(1024)
n = p * q
d = 65537
e = pow(d, -1, (p - 1) * (q - 1))
m = bytes_to_long(open("flag.txt", "rb").read())
c = pow(m, e, n)
open("10/output.txt", "w").write(f"{n = }\n{e = }\n{c = }\n")