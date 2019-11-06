import hashlib

file_path = input('Digite o caminho para o arquivo a ser validado \n')
hash = input('Digite o hash do arquivo \n')

with open(file_path, 'rb') as content_file:
    content = content_file.read()
    
hash_function_sha1 = hashlib.new('sha1')
hash_function_sha256 = hashlib.new('sha256')
hash_function_md5 = hashlib.new('md5')

hash_function_sha1.update(content)
hash_function_sha256.update(content)
hash_function_md5.update(content)

result = str(hash_function_sha1.hexdigest()) == hash or str(hash_function_sha256.hexdigest()) == hash or str(hash_function_md5.hexdigest()) == hash 
if(result):
    print("O arquivo está integro!")
else:
    print("o arquivo está não está integro :(")
