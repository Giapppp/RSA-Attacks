# Partial d exposure attack
from sage.all import *
from Crypto.Util.number import *
from tqdm import tqdm
import itertools

with open("9/output.txt", "r") as f:
    n = Integer(int(f.readline().split(" = ")[1]))
    e = Integer(int(f.readline().split(" = ")[1]))
    c = Integer(int(f.readline().split(" = ")[1]))
    leak = Integer(int(f.readline().split(" = ")[1]))

def small_roots(f, X, beta=1.0, m=None):
    N = f.parent().characteristic()
    delta = f.degree()
    if m is None:
        epsilon = RR(beta^2/f.degree() - log(2*X, N))
        m = max(beta**2/(delta * epsilon), 7*beta/delta).ceil()
    t = int((delta*m*(1/beta - 1)).floor())
    
    f = f.monic().change_ring(ZZ)
    P,(x,) = f.parent().objgens()
    g  = [x**j * N**(m-i) * f**i for i in range(m) for j in range(delta)]
    g.extend([x**i * f**m for i in range(t)]) 
    B = Matrix(ZZ, len(g), delta*m + max(delta,t))

    for i in range(B.nrows()):
        for j in range(g[i].degree()+1):
            B[i,j] = g[i][j]*X**j

    B =  B.LLL()
    f = sum([ZZ(B[0,i]//X**i)*x**i for i in range(B.ncols())])
    roots = set([f.base_ring()(r) for r,m in f.roots() if abs(r) <= X])
    return [root for root in roots if N.gcd(ZZ(f(root))) >= N**beta]
"""
Let t = number of bits of d_low
We have: 
    d * e = k * phi(n) + 1 = k * (n - p - q + 1) + 1
=>  leak * e = k * (n - p - q + 1) + 1 (mod 2^t)
=>  p * leak * e = k * (n * p - p^2 - n + p) + p (mod 2^t)
Because e is small enough, so we can bruteforce k and solve quadratic equation to get lsb of p
"""

t = (int(leak)).bit_length()
for k in tqdm(range(1, e)):
    P = PolynomialRing(Zp(2, t), 'x')
    x = P.gen()
    f = k * (n * x - x^2 - n + x) + x - x * leak * e
    for p_low, _ in f.roots():
        p_low = ZZ(p_low)
        p_hi = PolynomialRing(Zmod(n), 'p_hi').gen()
        p = p_hi * 2^t + p_low
        ans = small_roots(p.monic(), X=2^(1024 - t), beta = 0.5)
        if ans == []:
            continue
        p = int(p(ans[0]))
        q = n // p
        assert p * q == n
        d = pow(e, -1, (p - 1) * (q - 1))
        m = pow(c, d, n)
        try:
            print((long_to_bytes(m)).decode())
        except UnicodeDecodeError:
            continue
