# Based on CryptoCTF 2022 - Risk

from Crypto.Util.number import *

def genPrime(m, nbit):
	assert m >= 2
	while True:
		a = getRandomNBitInteger(nbit // m)
		r = getRandomNBitInteger(m ** 2 - m + 2)
		p = a ** m + r
		if isPrime(p):
			return (p, r)

nbit = 2048
e = 0x10001
p, rp = genPrime(4, nbit//2)
q, rq = genPrime(4, nbit//2)
n = p * q
m = bytes_to_long(open("flag.txt", "rb").read())
c = pow(m, e, n)
open("18/output.txt", "w").write(f"{n = }\n{e = }\n{c = }\n{rp = }\n{rq = }\n")