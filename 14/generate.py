from Crypto.Util.number import *

def gen_prime(nbit):
    number_of_primes = nbit//16
    while True:
        prime = 1
        for _ in range(number_of_primes):
            prime *= getPrime(16)
        if isPrime(2 * prime - 1):
            return 2 * prime - 1

p = gen_prime(1024)
q = getPrime(1024)
n = p * q
m = bytes_to_long(open("flag.txt", "rb").read())
e = 65537
c = pow(m, e, n)
open("14/output.txt", "w").write(f"{n = }\n{e = }\n{c = }\n")