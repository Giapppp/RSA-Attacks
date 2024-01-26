# William's p+1 method

from Crypto.Util.number import *
from sage.all import *
import itertools

with open("14/output.txt", "r") as f:
    n = Integer(int(f.readline().split(" = ")[1]))
    e = Integer(int(f.readline().split(" = ")[1]))
    c = Integer(int(f.readline().split(" = ")[1]))

def mlucas(v, a, n):
    v1, v2 = v, (v**2 - 2) % n
    for bit in bin(a)[3:]:
        v1, v2 = ((v1**2 - 2) % n, (v1*v2 - v) % n) if bit == "0" \
          else ((v1*v2 - v) % n, (v2**2 - 2) % n)
    return v1

def ilog(x, b):
    l = 0
    while x >= b:
        x //= b
        l += 1
    return l

def nth_root(x, n):
    # Start with some reasonable bounds around the nth root.
    upper_bound = 1
    while upper_bound ** n <= x:
        upper_bound *= 2
    lower_bound = upper_bound // 2
    # Keep searching for a better result as long as the bounds make sense.
    while lower_bound < upper_bound:
        mid = (lower_bound + upper_bound) // 2
        mid_nth = mid ** n
        if lower_bound < mid and mid_nth < x:
            lower_bound = mid
        elif upper_bound > mid and mid_nth > x:
            upper_bound = mid
        else:
            # Found perfect nth root.
            return mid
    return mid + 1

def attack(n):
    for v in itertools.count(1):
        for p in sieve_base:
            e = ilog(nth_root(n, 2), p)
            if e == 0:
                break
            for _ in range(e):
                v = mlucas(v, p, n)
            g = GCD(v - 2, n)
            if 1 < g < n:
                return g
            if g == n:
                break

p = attack(n)
q = n // p
assert p * q == n
d = pow(e, -1, (p - 1) * (q - 1))
m = pow(c, d, n)
print(long_to_bytes(m).decode())
