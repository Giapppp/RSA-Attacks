from Crypto.Util.number import *

nbit = 2048
p = getPrime(nbit//2)
q = getPrime(nbit//2)
n = p * q
d = getPrime(510) #Ensure that d < 1/3 * N^0.25
e = pow(d, -1, (p - 1) * (q - 1))
m = bytes_to_long(open("flag.txt", "rb").read())
c = pow(m, e, n)
open("11/output.txt", "w").write(f"{n = }\n{e = }\n{c = }\n")
