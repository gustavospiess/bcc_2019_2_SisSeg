import rsa
import pyaes

#get RSA private key
with open('privateKey.txt', 'rb') as content_file: 
    private_key = content_file.read()
    
#load the rsa public key from the content of the file
rsa_private_key = rsa.PrivateKey.load_pkcs1(private_key)
with open("AesKey.txt", 'rb') as content_file:
    aes_key_content = content_file.read()

#decrypt the AES key from de encrypted file content
aes_key = rsa.decrypt(aes_key_content, rsa_private_key)

#ask for the encryted file path
path = input("Type the path to the file to be decrypted: ")

#read the encrypted file
with open(path, 'rb') as content_file:
    content = content_file.read()

#decrypt the file
aes = pyaes.AESModeOfOperationCTR(aes_key)
decrypted = aes.decrypt(content).decode('utf-8')

#write the decrypted content to the file path given before
with open(path, 'w') as content_file:
    content_file.write(decrypted)


