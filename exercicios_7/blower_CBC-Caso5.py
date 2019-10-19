import blowfish
import os
BS = 8

pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
unpad = lambda s : s[0:-ord(s[-1])]
iv = os.urandom(8)
text = input("Escreva o texto para cifrar")

cipher = blowfish.Cipher("ABCDE".encode('ascii'))

cripted = b"".join(cipher.encrypt_cbc(pad(text).encode('utf-8'),iv))
print(cripted.hex())

decripted = unpad(b"".join(cipher.decrypt_cbc(cripted,iv)).decode('utf-8'))
print(decripted)
