from Crypto.Util.number import *

nbit = 2048
p = getPrime(1024)
q = getPrime(1024)
n = p*q

flag = open("flag.txt", "rb").read()
assert len(flag) == 17

message = f"Flag has two parts, the first one is {flag[:9]} and the second one is {flag[9:]}".encode()
m = bytes_to_long(message)
e = 5
d = pow(e, -1, (p - 1) * (q - 1))
c = pow(m, e, n)
assert pow(m, e) > n
assert m < n
open("20/output.txt", "w").write(f"{n = }\n{e = }\n{c = }\n")
