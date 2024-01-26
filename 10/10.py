# Small Private Exponent d attack
from Crypto.Util.number import *

with open("10/output.txt", "r") as f:
    n = int(f.readline().split(" = ")[1])
    e = int(f.readline().split(" = ")[1])
    c = int(f.readline().split(" = ")[1])

d = 1
while True:
    m = pow(c, d, n)
    try:
        print(long_to_bytes(m).decode())
    except UnicodeDecodeError:
        d += 1
    else:
        exit()