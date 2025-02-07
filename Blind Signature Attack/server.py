from Crypto.Util.number import *

nbits = 2048
p = getPrime(nbits//2)
q = getPrime(nbits//2)
n = p * q
e = 0x10001
d = pow(e, -1, (p - 1) * (q - 1))
m = bytes_to_long(open("flag.txt", "rb").read())

def menu():
    print("1. Get encrypted flag")
    print("2. Encrypt your message")
    print("3. Decrypt your message")
    print("4. Exit")
    option = int(input("> "))
    return option

print(f"Welcome to my RSA oracle. Here is my public key:\nn = {hex(n)}\ne = {hex(e)}\n")

while True:
    option = menu()
    if option == 1:
        print(f"Encrypted flag: {hex(pow(m, e, n))}")
    elif option == 2:
        message = int(input("Enter your message in hex: "), 16)
        print(f"Encrypted message: {hex(pow(message, e, n))}")
    elif option == 3:
        ciphertext = int(input("Enter your ciphertext in hex: "), 16)
        plaintext = pow(ciphertext, d, n)
        if plaintext == m:
            print("Nope")
        else:
            print(f"Decrypted message: {hex(plaintext)}")
    elif option == 4:
        print("Bye")
        exit()
    else:
        exit()