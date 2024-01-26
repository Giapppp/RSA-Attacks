from Crypto.Util.number import *
import random

def get_parameters():
    p = getPrime(1024)
    q = getPrime(1024)
    N = p*q
    phi = (p-1)*(q-1)
    while True:
        d = random.getrandbits(512)
        if (3*d)**4 > N and GCD(d,phi) == 1:
            e = inverse(d, phi)
            break
    return N,e

n, e = get_parameters()
m = bytes_to_long(open("flag.txt", "rb").read())
c = pow(m, e, n)
open("12/output.txt", "w").write(f"{n = }\n{e = }\n{c = }\n")
