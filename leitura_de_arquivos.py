"""
# Leitura de Arquivos:

- Para ler o conteúdo de um arquivo em Python, utilizamos a função
integrada 'open()' que literalmente significa abrir.

- open() => Na forma mais simples de utilização, passamos apenas um
parâmetro de entrada que, neste caso, é o caminho para o arquivo a
ser lido. Essa função retorna um _io.TextIOWrapper e é com ele que
trabalhamos.

Docs open() => https://docs.python.org/3/library/functions.html#open

Observação: Por padrão, a função open() abre o arquivo para leitura
- read. Dessa forma, o arquivo passado como argumento para ela deve
existir. Caso ele não exista, teremos o erro: FileNotFoundError.

"""

# Exemplo:
file = open('texto.txt')

print(f"file = {file}")
# Saída - output: file = <_io.TextIOWrapper name='texto.txt'
# mode='r' encoding='UTF-8'>

# Observações:
# 1) mode = 'r' => Modo de Leitura. r => read() => ler.
# 2) enconding='UTF-8' => A codificação em que o conteúdo do
# do arquivo foi escrito ou deve ser lido. No UTF-8, todos os
# acentos e caracteres especiais serão lidos.
# 3) name = 'texto.txt' => Nome do arquivo.

print(15*'-')
print(f"type(file) = {type(file)}")
# Saída - output: type(file) = <class '_io.TextIOWrapper'>
print(15*'-')

# Para ler o conteúdo de um arquivos após a sua abertura,
# devemos utilizar a função read():

# print(f"file.read() = {file.read()}")
# Saída - output: file.read() = Eu estou estudando na Geek University e
# estou aprendendo muito no curso de Programação em Python Essencial.
# print(15*'-')

# print(f"file.read() = {file.read()}")  # => Não retorna nada, pois
# do curso para a frente após a primeira leitura, não tem nada.
# print(15*'-')

# Observação:
# 1) O interpratdor Python utilizar um recurso para trabalhar com
# arquivos chamado 'cursor'. Este cursor funciona com um cursor quando
# estamos escrevendo.

# 2) A função read() lê t o d o o conteúdo o do arquivo.

ret = file.read()
print(f"type(ret) = {type(ret)}")  # => <class 'str'>
print(15*'-')
print(f"ret = {ret}")
print(15*'-')