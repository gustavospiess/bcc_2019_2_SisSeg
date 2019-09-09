# Desserialização de dados não confiáveis:

## Serialização e Desserialização:

Os processos de serialização são métodos para transformar dados em uma
sequência de bytes para armazenamento. Em python exemplos de processos de
serialização são as bibliotecas `pickle` e `dill`. O primeiro não serializa o
contexto junto dos objetos, então ao definir um objeto da classe `A`, é
necessário antes ter definido a própria classe. Esse processo gera arquivos
pequenos, que conseguem armazenar objetos de quaisquer espécie, desde que ao
carregá-los novamente, o façamos em um contexto onde as classes e funções
estáticas consumidas pelo objeto estejam disponíveis. Dessa forma, é simples
gravar um objeto em um método estático da própria classe, e carregá-lo da mesma
forma.

## Erros possíveis:

No entanto, esse processo, como apontado pela própria documentação, não é
segura. Isso se deve à arquitetura da biblioteca, que não fornecesse uma
interface para validarmos o que está sendo carregado em memória. Dessa forma,
recomenda-se que se utilize essa biblioteca apenas para importação de seriais
de fontes confiáveis.

## Alternativas:

Alternativamente, para armazenar grandes quantidades de dados em relativamente
pouco espaço, e estruturando de forma mais estável, tem-se as bibliotecas
`json` e `csv`. Essas bibliotecas fornecem estruturas mais estáveis, mas não
muito menos flexíveis no entanto.

Ao invés de serializar um objeto da classe desejada, pode-se gravar parâmetros
para um construtor ou método estático que instancie um novo objeto no mesmo
estado. Isso apresenta algumas dificuldades quanto se precisa serializar
objetos interdependentes, isso é, duas instâncias com referências mútuas. Nesse
caso, poderia ser realizada a gravação dos códigos hash dos objetos, ao invés
de uma referência explicita.

## Implementação:

Foram realizadas duas implementações, a [primeira](proj_item_1/) se refere a um
software em `python` bastante simples que realiza uma valoração de uma
expressão recebida por parâmetro e salva a mesma em um arquivo serial, também
parametrizável. Somado a ele, uma implementação de um software que faz a
leitura e a impressão desse arquivo.

```python
with open(file_path, 'ab') as file_buf:
    pickle.dump(datetime.datetime.now(), file_buf)
    pickle.dump(evaluated, file_buf)
```

Na exibição do arquivo, o código executado é:

```python
data = pickle.load(file_buf)
logging.info('Unpickled "%s"' % (str(data)))
if callable(data):
    logging.info('Executing it')
    data()
```

No entanto, com a passagem de um arquivo serializado de forma maliciosa, pode
ocorrer falha na segurança da aplicação, por exemplo com o arquivo
[untrusted.dmp](proj_item_1/untrusted.dmp), a mensagem produzida é:

```Bash
 > INFO:root:Info mode is on, general info is going to be printed
 > INFO:root:process started
 > INFO:root:Unpickled "<built-in function kill>"
 > INFO:root:Executing it
 > ERROR:root:Error unpickling
 > INFO:root:process concluded
```

Nesse caso controlado, não houveram danos reais, mas a execução desse código é
potencialmente perigosa, sendo que o arquivo vai construir objetos com
comportamentos próprios, quem podem consumir quaisquer informações e métodos
carregados dentro do contexto.

Na [Segunda](proj_item_2/) implementação, foi utilizada a biblioteca `json`
para resolver a mesma necessidade, dessa forma, é controlado quais códigos são
executados.

Tanto para a escrita:
```python
data = {'data': [*previous, {'date': repr(datetime.datetime.now()), 'info': evaluated}]}
json.dump(data, file_buf)
logging.debug('Writing JSON was successful')
```

Quanto para a leitura:
```python
data = json.load(file_buf)['data']
logging.info('read "%s"' % (str(data)))
for sub in data:
    info = sub['info']
    date = eval(sub['date'])
    logging.info('date "%s"' % (str(date)))
    logging.info('processing "%s"' % (str(info)))
    if callable(info):
        logging.info('Executing it')
        info()
```

Claro, a implementação apresenta ainda uma série de ouras vulnerabilidades,
tanto na construção do arquivo quanto na leitura do mesmo, códigos podem ser
dinamicamente executados, o que representa uma segunda ameaça.  No entanto,
nesse contexto seria mais simples alterar a configuração para carregar
estritamente a data, salvando como um número e depois inicializando ele n
construtor da classe `datetime`. Mas a intenção era demonstrar a fragilidade da
biblioteca `pickle` e uma solução preliminar com a biblioteca `json`.

## Referências:

 - [pickle - Python object serialization](https://docs.python.org/2/library/pickle.html)
 - [Deserialization of Untrusted Data](https://snyk.io/vuln/SNYK-JAVA-COMFASTERXMLJACKSONCORE-72445)
 - [CWE-502: Deserialization of Untrusted Data](https://cwe.mitre.org/data/definitions/502.html)
