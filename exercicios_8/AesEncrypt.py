import pyaes
import rsa

key = "This_key_is__a__complete_mystery"
#ask for the path of the file to be encrypted
path = input("Type the path to the file to be encrypted: ")
#read the file 
with open(path, 'r') as content_file:
    content = content_file.read()
#set encode the key
key = key.encode('utf-8')

aes = pyaes.AESModeOfOperationCTR(key)

#encrypt text with AES
ciphertext = aes.encrypt(content)

#write the encrypted text to the file
with open(path, 'wb') as content_file:
    content_file.write(ciphertext)
    
#set the AES key as the message to cypher with RSA
message = key

#get RSA public key
with open('publicKey.txt', 'rb') as content_file: 
    public_key = content_file.read()
    
# load the rsa public key from the content of the file
rsa_public_key = rsa.PublicKey.load_pkcs1(public_key)

#encrypt AES key with RSA public key
crypto = rsa.encrypt(message, rsa_public_key)

#write the encrypted key to a file
with open('AesKey.txt', 'wb') as content_file:
    content_file.write(crypto)
