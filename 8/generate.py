from Crypto.Util.number import *

nbit = 2048
p = getPrime(nbit//2)
q = getPrime(nbit//2)
e = getPrime(128)
n = p * q
m = bytes_to_long(open("flag.txt", "rb").read())
c = pow(m, e, n)
leak = p >> 480
open("8/output.txt", "w").write(f"{n = }\n{e = }\n{c = }\n{leak = }")