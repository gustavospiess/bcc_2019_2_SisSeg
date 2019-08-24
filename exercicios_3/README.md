# Execício 03

## Sobre a implementação:
Os itens do trabalho foram implementados utilizando:
- `Python 3.7.4`
- A execução foi realizada através do `Windows cmd`
- Sistema operacional `Windows 10`

O sistema possibilita a criação de pastas recebendo um nome.

## Execução:

O software é executado diretamente a partir do terminal, com o comando:

```shell
python3 mkdir.py
```

O diretório de execução deve ser um dos diretórios dos itens.

Será solicitado um nome de diretório a fim de ser criado. Exemplos de Shell
Injection nesse caso seriam: `pasta2 & rd pasta1` ou `pasta2 & shutdown -s -f`.
Se informado um nome válido, será criado uma pasta com esse nome no diretório
de execução do programa.

Os diferentes itens terão comportamentos distintos para casos de exceção.

## Itens:

### Item 1
![Tela do console + Navegador do arquivo, shell injection ](proj_item_1/Evidencia.png)

Foi utilizada a estratégia de shell injection para excluir uma determinada pasta.
O trecho de código segue:
```Python
os.system("md " + comando_str)
```

Com a passagem de parâmetros da imagem, o comando executado será:
```shell
md pasta2 & rd pasta1
```

Dessa forma, ao criar uma pasta `pasta2`, será executada a exclusão da pasta
`pasta1`.

### Item 2
![Tela do console, validação com white list](proj_item_2/Evidencia.png)

Nesse caso, foi realizada a validação por meio de `white list`, isso é, se os
parâmetros não estivessem adequadamente informados, não respeitando o que era
pedido, não é possível executar o comando shell.

O código da validação segue:
```python
    comando_str = input('Diretorio: ')
    match = re.fullmatch(_directory_regex,comando_str)
    if not match:
        print('Diretório Inválido, é permitido letras, numeros, ".", "/", "\" e ":" ')
        input();
        return
    os.system("md " + comando_str)
```

Dessa forma, se o usuário tentar informar algum valor que não se enquadre
estritamente no que é solicitado, não sendo a descrição adequada de uma pasta,
o processo é descontinuado e é apresentada uma message.

A passagem dos parâmetros errados resulta em uma mensagem:
```shell
> Diretório Inválido, é permitido letras, numeros, ".", "/", "\" e ":"
```

### Item 3
![Tela do console, com uso de API segura](proj_item_3/Evidencia.png)

Neste último caso, é realizada a execução com a API do python para construção
de diretórios. Isso é, o nome informado pelo usuário é adequadamente tratado
para a construção do diretório.

A validação é feita com o seguinte trecho de código:
```python
    os.mkdir(comando_str)
```

Dessa forma, ao inserir os dados maliciosos, será executada o comando:

```shell
md "pasta2 & rd pasta1"
```
