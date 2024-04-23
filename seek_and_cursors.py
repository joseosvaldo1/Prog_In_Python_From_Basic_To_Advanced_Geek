"""
# Seek e Cursors:

- seek() => É utilizada para movimentar o cursor pelo arquivo.

# ------------------------------------------------------------------


file = open('texto.txt')
print(15*'-')
print(file.read())
print(15*'-')
print(file.read())
print(15*'-')


# seek() => A função seek() é utilizada para movimentar o cursor
# pelo arquivo. Ela recebe um parâmetro que indica onde queremos
# colocar o cursor.

# Movimentando o cursor com a função seek():
file.seek(0)
print(15*'-')
print(file.read())
print(15*'-')

file.seek(22)
print(15*'-')
print(file.read())
print(15*'-')

# seek => traduzindo do inglês, significa "procurar".
file.close()


# -------------------------------------------------------------------


# readline() => função que lê o arquivo linha a linha. Este método lê
# uma única linha do arquivo e avança o "cursor" para a próxima linha.
# Se chamado novamente, ele lê a próxima linha e assim por diante até o
# final do arquivo. Retorna uma string contendo a linha lida.

file = open('texto.txt')
# print(15*'-')
# print()
# print('1ª linha:')
# print(file.readline())  # 1ª linha
# print(15*'-')
# print('2ª linha:')
# print(file.readline())  # 2ª linha
# print(15*'-')
# print('3ª linha:')
# print(file.readline())  # 3ª linha
# print(15*'-')
# print('4ª linha:')
# print(file.readline())  # 3ª linha
# print(15*'-')

retorno = file.readline()
print(f"retorno = {retorno}")
print(15*'-')
print(f"type(retorno) = {type(retorno)}")
print(15*'-')
print(f"retorno.split(' ') = {retorno.split(' ')}")
print(15*'-')


# -------------------------------------------------------------------

# readlines() => Este método lê todas as linhas do arquivo e as armazena
# em uma lista. Cada elemento da lista corresponde a uma linha do arquivo.
# Ao final da leitura, o cursor está no final do arquivo. Retorna uma
# lista de strings, cada uma representando uma linha do arquivo.

file = open('texto.txt')
print(f"Total de linhas: len(texto) = {len(file.readlines())}")
print(f"file.readlines() = {file.readlines()}")

# -------------------------------------------------------------------

"""


# readlines() => Este método lê todas as linhas do arquivo e as armazena
# em uma lista. Cada elemento da lista corresponde a uma linha do arquivo.
# Ao final da leitura, o cursor está no final do arquivo. Retorna uma
# lista de strings, cada uma representando uma linha do arquivo.

# Observação: Quando abrimos um arquivo com a função 'open()', é criada
# uma conexão entre o arquivo no disco do cumputador e o nosso programa.
# Essa concexão é chamada de streaming. Ao finalizar os trabalhos com o
# arquivo, devemos fechar essa conexão. Para isso, utilizamos a função
# 'close()'.

# Passos para se trabalhar com um arquivo:
# 1º Abrir o arquivo;
file = open('texto.txt')

# 2º Trabalhar/manipular o arquivo;

print(f"Os primeiros 50 caracteres do texto - file.read(50): "
	  f"{file.read(50)}")
# Saída: Eu estou estudando na Geek University e estou apre

# Observação: Com a função read() e um argumento inteiro,
# podemos limitar a quantidade de caracteres a serem lidos.

print(f"Total de linhas: len(texto) = {len(file.readlines())}")
print(f"file.readlines() = {file.readlines()}")
print("Antes de fecharmos o arquivo: ")
print(f"file.closed = {file.closed}") # => False
# Observação: o método 'closed' verifica se um dado arquivo
# está aberto (False) ou fechado (True).



# 3º Fechar o arquivo.
file.close()
print("Depois de fecharmos o arquivo: ")
print(f"file.closed = {file.closed}")  # => True

# Fechar arquivos com close() no Python é importante por vários motivos:

# Libera recursos do sistema: Quando um arquivo é aberto, o Python aloca
# recursos do sistema, como memória e descritores de arquivo. Fechar o
# arquivo libera esses recursos, permitindo que sejam usados por outros
# programas.
# Evita corrupção de dados: Se um arquivo não for fechado corretamente,
# os dados nele contidos podem ser corrompidos. Isso pode ocorrer se o
# programa travar ou se o sistema operacional for desligado inesperadamente.
# Melhora o desempenho: Manter muitos arquivos abertos pode prejudicar o
# desempenho do programa, especialmente em sistemas com recursos limitados.
# Fechar arquivos que não estão mais sendo usados libera memória e melhora
# a velocidade geral do programa.
# Cumpre as melhores práticas: É considerado uma boa prática fechar arquivos
# quando terminar de usá-los. Isso ajuda a manter seu código limpo e
# organizado e evita possíveis problemas.

# Observação: Se tentarmos manipular um arquivo após o seu fechamento,
# obteremos um erro: ValueError.