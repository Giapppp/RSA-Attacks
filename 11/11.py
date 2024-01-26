#Wiener's Attack
from Crypto.Util.number import *
from sage.all import *

with open("11/output.txt", "r") as f:
    n = int(f.readline().split(" = ")[1])
    e = int(f.readline().split(" = ")[1])
    c = int(f.readline().split(" = ")[1])

#Continued fraction
def fraction(p, q):
    a = []
    while q:
        a.append(p // q)
        p, q = q, p % q
    return a

#Convergents
def convergents(a):
    p = [0, 1]
    q = [1, 0]
    for it in a:
        p.append(p[-1]*it + p[-2])
        q.append(q[-1]*it + q[-2])
    return p, q

#Attack
def attack(e, n):
    cf = fraction(e, n)
    numerators, denominators = convergents(cf)
    for k, d in zip(numerators, denominators):
        if k == 0 or d%2 == 0 or e*d % k != 1:
            continue
        phi = (e*d - 1)//k
        x = PolynomialRing(RationalField(), 'x').gen()
        f = x**2 - (n - phi + 1) * x + n
        roots = f.roots()
        if len(roots) != 2:
            continue
        p = int(roots[0][0])
        q = int(roots[1][0])
        if n == p * q:
            return d
    return None

d = attack(e, n)
m = pow(c, d, n)
print(long_to_bytes(m).decode())