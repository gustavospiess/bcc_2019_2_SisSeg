# Execício 08

## Sobre a implementação:
Os itens do trabalho foram implementados utilizando:
- `Python 3.7.4`
- A execução foi realizada através do `Windows cmd`
- Sistema operacional `Windows 10`

O sistema possibilita criptografia de um arquivo pelo algoritmo AES, criptografa a chave do AES com a chave pública do Algoritmo RSA e possibilita descriptografar o arquivo criptografado anteriormente, descriptografando a chave do AES e depois usando ela para descriptografar o arquivo.

## Execução:

O software é executado pelos arquivos:

```
GenerateRsaKeys.py
AesEncrypt.py
AesDecrypt.py
```
O diretório de execução é o diretório do exercício 8.

## Sequência de execução
### GenerateRsaKeys
Ao executalo será gravado no arquivo `privateKey.txt` a chave privada, em `publicKey.txt` a chave publica e em `params.txt` as informações de expoente de ambas as chaves e o módulo

segue exemplo resultante da execução:
`privatekey.txt`
```
----BEGIN RSA PRIVATE KEY-----
MIIBPAIBAAJBAIkmvZ4Xl/ji4Zd6Mvdj7PClv12MEwsYn9QMeAg44dS07+sDoRkO
ROMX8sXZX+/FFf23SSceoGQm8NsrpXQNJ3sCAwEAAQJBAIUCg0Z8zy/aqLnFEwSF
blZ8CDjrDdTnDqoRZZ9jumkp0etb7+78/9BbTLxFn90XIRCkBDCnfLNQKsTaEVbI
vVECIwCLHh1/CsEybEgSWmd467yNXskR49Hmm8beavMQWviheqKlAh8A/GG0pt/E
9WXDUgsIiPaXAxAvfaoajPZWMLrNvyefAiJXFlkcqFzc9dAAPTu9BMWaMhXo7xb9
J9NMdOMIAArY+25JAh5QtHnNRw83ndQIv0h6a8g8jYdyOtwEqZ1ENegnMWcCIhXn
wYSCti+eX25au5pqjbQeOhQNYJJRZ2gRSEMsg4xHDXo=
-----END RSA PRIVATE KEY-----
```

`publickey.txt`
```
-----BEGIN RSA PUBLIC KEY-----
MEgCQQCJJr2eF5f44uGXejL3Y+zwpb9djBMLGJ/UDHgIOOHUtO/rA6EZDkTjF/LF
2V/vxRX9t0knHqBkJvDbK6V0DSd7AgMBAAE=
-----END RSA PUBLIC KEY-----
```

`params.txt`
```
Expoente da chave Privada:
6966289298432724953915012154900579291591084257285020872064240488242859000550468498426452034343324016292133916151026407744222931901874532250437638475529553

Expoente da chave Publica:
65537

Módulo:
7183198051407934411163475118721785849664949950748739936632274912331606573227266743442184318150559052989042825433098906076867927730335070712412613771077499
```
Após de gerado as chaves deve ser executado o arquivo `AesEncrypt.py``

### AesEncrypt
Ao executa-lo sera pedido um caminho de um arquivo para criptografar,
como exemplo foi usado o caminho `TestFile.txt` que está na própria pasta junto com as classes segue seu conteúdo:
```
Isso é um belo teste
```
Com isso o arquivo será criptografádo usando a chave `This_key_is__a__complete_mystery`
e o conteúdo criptografado irá sobreescrever o conteudo do arquivo `TestFile.txt`
ficando:
```
˜ ßÎ˜˜aÇ]¾‰ë2††‘ìW†
```
Também será criptografado a chave do algoritmo `AES` mencionada acima usando a `publicKey` do algoritmo `RSA` e ela será escrita no arquivo `AesKey.txt` seu conteúdo é:
```
Rw˜ñ	v^Ì(C›øX]MÍs+N<WßŸá˜ŽT,x…íÊþ%ŽC­#KQKë¼,kÈ™Ÿô*¬ðâR÷sdâe
```
Finalmente poderemos executar o arquivo `AesDecrypt.py` que irá descriptografar o arquivo
### AesDecrypt
Esse irá solicitar o caminho de um arquivo criptografado nesse caso passei:
```
TestFile.txt
```
ou seja o arquivo que foi criptografado anteiormente.  
Entao será utilizado a `privateKey` do algotimo `RSA` para descriptografar a chave do algoritmo `AES` e então sera descriptografado o conteúdo do arquivo `TestFile.txt` que ficará como:
```
Isso é um belo teste
```
