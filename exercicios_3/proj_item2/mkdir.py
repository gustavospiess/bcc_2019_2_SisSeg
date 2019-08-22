import os
import re

def main():
    _directory_regex = re.compile('[a-zà-ú]|[A-ZÀ-Ú]|\/|\\|\s|\.|[0-9]|:')
    comando_str = input('Diretorio: ')
    match = re.fullmatch(_directory_regex,comando_str)
    if not match:
        print('Diretório Inválido, é permitido letras, numeros, ".", "/", "\" e ":" ')
        input();
        return
    os.system("md " + comando_str)
    

if __name__ == '__main__':
    main()
