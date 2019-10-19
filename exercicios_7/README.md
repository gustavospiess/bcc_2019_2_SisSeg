
# Caso 1
Criptografe o texto “FURB” usando o modo de operação “ECB”.
## 1.1. Qual o conteúdo do texto cifrado (em hexadecimal)?
7f4700aa6f5fe08b
## 1.2. Qual a extensão (quantidade de caracteres) do texto cifrado?
16 caracteres
# Caso 2

Criptografe “COMPUTADOR” e o modo de operação “ECB”.

## 2.1. Qual o conteúdo do texto cifrado (em hexadecimal)?
f34739ab7634c4efe50ff1b554856572
## 2.2. Qual a extensão do texto cifrado?
32 caracteres
## 2.3. Por que o texto cifrado tem tal tamanho?
Pois o tamanho de cada bloco é 8 bits e a palavra computador possui 10 letras com isso é necessário quebrar ela em 2 blocos

# Caso 3
Criptografe “SABONETE” e utilize o modo de operação “ECB”.

## 3.1. Qual o conteúdo do texto cifrado (em hexadecimal)?
841091472604b96acdbc3e2fefa73bdd
## 3.2. Qual a extensão do texto cifrado?
32 caracteres
## 3.3. Por que o texto cifrado tem tal tamanho?

# Caso 4
Criptografe o texto “SABONETESABONETESABONETE” e utilize o modo de operação “ECB”.

## 4.1. Qual o conteúdo do texto cifrado (em hexadecimal)?
841091472604b96a841091472604b96a841091472604b96acdbc3e2fefa73bdd

## 4.2. Qual a extensão do texto cifrado?
64 caracteres

## 4.3. Avalie o conteúdo do texto cifrado. Que conclusão é possível obter a partir do texto cifrado e do texto simples?
841091472604b96a SABONETE  
841091472604b96a SABONETE  
841091472604b96a SABONETE  
cdbc3e2fefa73bdd
É possível verificar que a palavra "SABONETE" nessa conversão equivale a "841091472604b96a" 

# Caso 5
Criptografe o texto “FURB” e agora utilize o modo de operação “CBC”.

## 5.1. Qual o conteúdo do texto cifrado (em hexadecimal)?
983d09b53fe271f9
## 5.2. Tente decifrar o texto cifrado, para recuperar o texto simples. O que acontece?
Ele exige um vetor de inicialização, porem ao ser usado ele retorna o texto "FURB"

# Caso 6
Criptografe o texto “FURB”, utilizando o modo de operação “CBC”. Estabeleça que o vetor de inicialização seja

constituído dos bytes: 1, 1, 2, 2, 3, 3, 4, 4.

## 6.1. Qual o conteúdo do texto cifrado?
cf0a75a354fb624c
# Caso 7
Criptografe o texto “SABONETESABONETESABONETE” e utilize o modo de operação “CBC”. Defina o vetor de
inicialização constituído dos bytes 1, 1, 2, 2, 3, 3, 4, 4.

## 7.1. Qual o conteúdo do texto cifrado (em hexadecimal)?
9b1813dacaf2d6509d10c55c33f36b0918d49bf6cd0c1241e1ab6d1d3119eab6

## 7.2. Compare o texto cifrado com aquele obtido no #Caso 4 e apresente uma conclusão desta comparação.
Caso 4 - 841091472604b96a841091472604b96a841091472604b96acdbc3e2fefa73bdd  
Caso 7 - 9b1813dacaf2d6509d10c55c33f36b0918d49bf6cd0c1241e1ab6d1d3119eab6  
Pode ser concluido que foi gerado um texto cifrado onde não há a repetição que havia no caso 4

# Caso 8
Criptografe o texto “SABONETESABONETESABONETE” e utilize o modo de operação “CBC”. Defina o vetor de
inicialização constituído dos bytes 10,20,30,40,50,60,70,80.

## 8.1. Qual o conteúdo do texto cifrado?
10981fe3009f1fe0ab7592179c361cc7af8eb390b79ebc8ed6a1f71d43e1c0c4

## 8.2. Compare o texto cifrado com o que foi obtido no #Caso 7 e apresente conclusão sobre a comparação.
Caso 7 - 9b1813dacaf2d6509d10c55c33f36b0918d49bf6cd0c1241e1ab6d1d3119eab6  
Caso 8 - 10981fe3009f1fe0ab7592179c361cc7af8eb390b79ebc8ed6a1f71d43e1c0c4  
Pode ser concluido que o resultado é diferente para cada cifragem

## 8.3. A partir do resultado de 8.2, decriptografe a mensagem usando o vetor de inicialização constituído dos bytes 1, 1,2, 2, 3, 3, 4, 4. Qual a conclusão que você atinge?
Resultado: XT^ezSABONETESABONETE  
A conclusão atingida é que mesmo com o vetor de inicialização incorreto é possível identificar uma parte da mensagem criptografada desde que se tenha a chave correta.

# Caso 9
## 9.1. Criptografe o texto “FURB” usando o modo de operação “ECB”. A partir do texto cifrado obtido, tente decifrá-lo utilizando a chave “11111”. Explique o resultado.
É apresentado a seguinte mensagem:  
´UnicodeDecodeError: 'utf-8' codec can't decode byte 0x9d in position 0: invalid start byte´  
Ou seja foi tentado transformar em um caracter 'utf-8' um 'byte' inválido, obtido através da conversão por uma chave errada.



