import blowfish
import os
BS = 8
iv = bytearray([10,20,30,40,50,60,70,80])
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
unpad = lambda s : s[0:-ord(s[-1])]
text = input("Escreva o texto para cifrar")

cipher = blowfish.Cipher("ABCDE".encode('ascii'))

cripted = b"".join(cipher.encrypt_cbc(pad(text).encode('utf-8'),iv))
print(cripted.hex())
iv2 = bytearray([1, 1, 2, 2, 3, 3, 4, 4])
decripted = unpad(b"".join(cipher.decrypt_cbc(cripted,iv2)).decode('utf-8'))
print(decripted)
