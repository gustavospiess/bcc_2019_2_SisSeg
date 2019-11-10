from AES import generate_round_keys,cyfer

def main():
    crypted = []
    key = []
    while(len(key) != 16):
        key = input('Digite uma chave com 16 caracteres').split(',')
    
    num_key = [int(x) for x in key]
    round_key_0 =[num_key[0], num_key[1], num_key[2], num_key[3]],[num_key[4], num_key[5], num_key[6], num_key[7]],[num_key[8], num_key[9], num_key[10], num_key[11]],[num_key[12], num_key[13], num_key[14], num_key[15]]
    round_key_list = generate_round_keys(round_key_0)
    
    path = input('Digite o caminho do arquivo a ser cifrado')
    with open(path, 'r') as content_file: 
        text = content_file.read()
        
    text.encode('ascii')    
    n = 16
    textList = [(text[i:i+n]) for i in range(0, len(text), n)] 
    if(len(textList[-1]) % 16 != 0):
        size = 16 - len(textList[-1])
        for i in range(size):
            textList[-1] += str(size)
        
    for i in range(len(textList)):
       crypted += cyfer(textList[i].encode('ascii'),round_key_list)

    path = input('escolha o nome do arquivo a ser gerado: \n')
    with open(path, 'wb') as content_file:
        for i in range(len(crypted)):
            content_file.write(str(crypted[i]).encode('utf-8'))

if __name__ == '__main__':
    main()
