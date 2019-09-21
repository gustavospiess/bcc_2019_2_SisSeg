def main():
    novo_texto = ""
    resposta = input("Digite 'D' para decifrar e 'C' cifrar: ")
    if(resposta == 'D' or resposta == 'd'):
        texto = input("insira o texto para decifrar: ")
        for letra in texto:
            if(letra == 'a'):
                novo_texto += 'x'
            if(letra == 'A'):
                novo_texto += 'X'
            if(letra == 'b'):
                novo_texto += 'y'
            if(letra == 'B'):
                novo_texto += 'Y'
            if(letra == 'c'):
                novo_texto += 'z'
            if(letra == 'C'):
                novo_texto += 'Z'
            if(letra == ' '):
                novo_texto += ' '
                
            if not(letra in ['a','b','c','A','B','C',' ']):
                if((ord(letra) >= 65 and ord(letra) <= 90) or (ord(letra) >= 97 and ord(letra) <= 122)):
                    novo_texto += chr(ord(letra)-3)    

        print("o texto decifrado é: " + novo_texto)
        input()

    if(resposta == 'C' or resposta == 'c'):
        texto = input("insira o texto para cifrar: ")
        for letra in texto:
            if(letra == 'x'):
                novo_texto += 'a'
            if(letra == 'X'):
                novo_texto += 'A'
            if(letra == 'y'):
                novo_texto += 'b'
            if(letra == 'Y'):
                novo_texto += 'B'
            if(letra == 'z'):
                novo_texto += 'c'
            if(letra == 'Z'):
                novo_texto += 'C'
            if(letra == ' '):
                novo_texto += ' '
                
            if not(letra in ['z','x','y','Z','X','Y',' ']):
                if((ord(letra) >= 65 and ord(letra) <= 90) or (ord(letra) >= 97 and ord(letra) <= 122)):
                    novo_texto += chr(ord(letra)+3)
                

        print("o texto cifrado é: " + novo_texto)
        input()
    
if __name__ == "__main__":
    main()
