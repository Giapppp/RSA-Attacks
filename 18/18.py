# Special Prime form p = a^m + r_p
# Resource: Ghafar AHA. et al., "A New LSB Attack on Special-Structured RSA Primes"

from Crypto.Util.number import *
from math import ceil
from sage.all import ZZ
from sage.all import sqrt

with open("18/output.txt", "r") as f:
    n = int(f.readline().split(" = ")[1])
    e = int(f.readline().split(" = ")[1])
    c = int(f.readline().split(" = ")[1])
    rp = int(f.readline().split(" = ")[1])
    rq = int(f.readline().split(" = ")[1])


def attack(N, rp, rq):
    i = ceil(sqrt(rp * rq))
    x = ZZ["x"].gen()
    while True:
        sigma = (round(int(sqrt(N))) - i) ** 2
        z = (N - (rp * rq)) % sigma
        f = x ** 2 - z * x + sigma * rp * rq
        for x0 in f.roots(multiplicities=False):
            if x0 % rp == 0:
                p = int((x0 // rp) + rq)
                assert N % p == 0
                return p, N // p
            if x0 % rq == 0:
                p = int((x0 // rq) + rp)
                assert N % p == 0
                return p, N // p

        i += 1

p, q = attack(n, rp, rq)
d = pow(e, -1, (p - 1) * (q - 1))
m = pow(c, d, n)
print(long_to_bytes(m).decode())