import os

def main():
    comando_str = input('Diretorio: ')
    os.system("md " + comando_str)

if __name__ == '__main__':
    main()
