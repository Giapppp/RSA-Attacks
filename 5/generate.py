#Generate e triples (e, N_i, C_i)
from Crypto.Util.number import *

open("5/output.txt", "w")
e = 17
m = bytes_to_long(open("flag.txt", "rb").read())
for _ in range(e):
    p = getPrime(512)
    q = getPrime(512)
    N = p * q
    C = pow(m, e, N)
    with open("5/output.txt", "a") as f:
        text = f"{e = }\n{N = }\n{C = }\n"
        f.write(text)
