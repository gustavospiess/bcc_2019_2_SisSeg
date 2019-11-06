import hashlib

choice = input('Digite o numero do modo selecionado:\n 1 - sha1\n 2 - sha256\n 3 - md5\n')
path = input('Digite o caminho para o arquivo a ser gerado o hash \n')

with open(path, 'rb') as content_file:
    content = content_file.read()
    
if(int(choice) ==  1):
    hash_function = hashlib.new('sha1')
elif(int(choice) == 2):
    hash_function = hashlib.new('sha256')
elif(int(choice) == 3):
    hash_function = hashlib.new('md5')


hash_function.update(content)
result = hash_function.hexdigest()
print(result)
input()
