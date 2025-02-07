from Crypto.Util.number import *
import random

e = 0x10001

def get_primorial(n):
    result = 1
    for i in range(n):
        result = result * sieve_base[i]
    return result


def get_fast_prime():
    M = get_primorial(40)
    while True:
        k = random.randint(2**28, 2**29-1)
        a = random.randint(2**20, 2**62-1)
        p = k * M + pow(e, a, M)

        if isPrime(p):
            return p
        
p = get_fast_prime()
q = get_fast_prime()
n = p * q
m = bytes_to_long(open("flag.txt", "rb").read())
c = pow(m, e, n)
open("17/output.txt", "w").write(f"{n = }\n{e = }\n{c = }\n")