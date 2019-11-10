import rsa
from hashlib import sha512


#ask for the path of the file to be signed
path = input("Type the path to the file to be signed: ")
#read the file 
with open(path, 'rb') as content_file:
    content = content_file.read()

#get RSA private key
with open('privateKeyA.txt', 'rb') as content_file: 
    private_key = content_file.read()
    
#load the rsa private key from the content of the file
rsa_private_key = rsa.PrivateKey.load_pkcs1(private_key)


hash = int.from_bytes(sha512(content).digest(), byteorder='big')
# raise the hash to the power d modulo n 
signature = pow(hash, rsa_private_key.d, rsa_private_key.n)

#write the signature to the file
with open('signature.txt', 'wb') as content_file:
    content_file.write(str(signature).encode('utf-8'))
