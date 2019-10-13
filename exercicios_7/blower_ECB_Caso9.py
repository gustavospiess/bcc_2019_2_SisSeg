import blowfish

BS = 8

pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
unpad = lambda s : s[0:-ord(s[-1])]

text = input("Escreva o texto para cifrar")
cipher = blowfish.Cipher("ABCDE".encode('ascii'))
cripted = b"".join(cipher.encrypt_ecb(pad(text).encode('utf-8')))
print(cripted.hex())
decipher = blowfish.Cipher("11111".encode('ascii'))
decripted = unpad(b"".join(decipher.decrypt_ecb(cripted)).decode('utf-8'))
print(decripted)
