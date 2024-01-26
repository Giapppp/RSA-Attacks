# Blind Signature Attack

from Crypto.Util.number import *
from pwn import *

target = process(["python3", "16/server.py"])

target.recvline()
n = int(target.recvline().decode().split(" = ")[1], 16)
e = int(target.recvline().decode().split(" = ")[1], 16)

#Get encrypted flag
for _ in range(4):
    target.recvline()
target.sendlineafter(b"> ", b"1")
flag_enc = int(target.recvline().decode().split(": ")[1], 16)

fake_flag_enc = (flag_enc * pow(2, e, n)) % n

#Get decrypted fake flag
for _ in range(4):
    target.recvline()
target.sendlineafter(b"> ", b"3")
target.sendlineafter(b"Enter your ciphertext in hex: ", hex(fake_flag_enc))
fake_flag_dec = int(target.recvline().decode().split(":")[1], 16)

#Get real flag
flag = (fake_flag_dec * pow(2, -1, n)) % n
print(long_to_bytes(flag).decode())
target.close()