from Crypto.Util.number import *

nbit = 2048
p = getPrime(nbit//2)
q = getPrime(nbit//2)
n = p * q

flag = open("flag.txt", "rb").read()
plaintext = b"Merry Christmas and Happy New Year! I won't talk to you that the flag is: " + flag
assert len(flag) == 17
m = bytes_to_long(plaintext)
e = 3
c = pow(m, e, n)
assert pow(m, e) > n
assert m < n
open("19/output.txt", "w").write(f"{n = }\n{e = }\n{c = }\n")