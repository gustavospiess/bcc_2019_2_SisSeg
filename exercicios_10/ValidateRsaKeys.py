import rsa
import pyaes
from hashlib import sha512

#ask for the path of the file to be validated
path = input("Type the path to the file to be validated: ")
#read the file 
with open(path, 'rb') as content_file:
    content = content_file.read()

path = input("Type the path to the Pulbic key file: ")
#get RSA public key
with open(path, 'rb') as content_file: 
    public_key = content_file.read()
    
#get signature
with open('signature.txt', 'rb') as content_file: 
    signature = content_file.read()

    
# load the rsa public key from the content of the file
rsa_public_key = rsa.PublicKey.load_pkcs1(public_key)

#get message hash
hash = int.from_bytes(sha512(content).digest(), byteorder='big')

#raise the signature to power e modulo n
hashFromSignature = pow(int(signature.decode('utf-8')), rsa_public_key.e, rsa_public_key.n)

if(hash == hashFromSignature):
    print("a assinatura é válida")
else:
    print("a assinatura não é válida ou o arquivo foi adulterado")
