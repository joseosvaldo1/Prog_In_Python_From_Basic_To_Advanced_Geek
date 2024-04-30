"""
# Modos de Abertura de Arquivos:

'r' => abre para leitura (padrão)

'w' => abre para gravação, truncando (sobrescrevendo)
caso o primeiro arquivo já exista.

'x' => abre para criação exclusiva, falhando se o arquivo já existir.
Abre para a escrita somente se o arquivo não existir. Caso o arquivo
exista, gera um erro: FileExistsError.

'a' => abre para escrita, acrescentando ao final do arquivo se o
mesmo já existir.

'b' => modo binário

't' => modo de texto (padrão)

'+' => abre para atualização (leitura e escrita). Deve vir sempre
acompanhado de outro modo ('r+', 'x+', 'w+', 'a+', etc.). Nele,
temos o controle do cursor usando com o modo 'r' ou 'w'.



# -----------------------------------------------------------------


# Exemplo usando o modo 'x' de open():

# Usando inicialmente a função open() no modo 'x':
# with open('university.txt', 'x') as file_x:
# 	file_x.write("Teste de conteúdo - modo 'x' de open().")

# Saída - 1ª execução: Criou o arquivo 'university.txt' com o
# seguinte conteúdo: "Teste de conteúdo - modo 'x' de open()."

# Saída - 2ª execução: Como o arquivo 'university.txt' já existe,
# pois foi criada na primeira execução, teremos um erro:
# FileExistsError: [Errno 17] File exists: 'university.txt'


# Usando a função open() no modo 'x' com try/except:

# try:
# 	with open('university.txt', 'x') as file_x:
# 		file_x.write("Teste de conteúdo - modo 'x' de open().")
#
# except FileExistsError:
# 	print("The file already exists.")


# -----------------------------------------------------------------


# Exemplo usando o modo 'a' de open():
# Exemplo_A:


with open('frutas.txt', 'a') as file_a:
	while True:
		fruit = input("Enter a name for a fruit or type 'sair' to quit: ")
		if fruit != 'sair'.lower():
			file_a.write(fruit)
			file_a.write('\n')
		else:
			break

# Observação: Abrindo no mode 'a' (append) da função 'open()',
# o arquivo será criado caso não exista. Caso contrário, o novo
# conteúdo será adicionado ao final do mesmo.


# ------------------------------------------------------------

"""

# Exemplo_B:
# Tentando adicionar no início do arquivo:


# with open('outro.txt', 'a') as file_a:
# 	file_a.seek(0)
# 	file_a.write('No topo.\n')
# 	file_a.write('Nova linha.\n')
# 	file_a.write('Mais uma linha.\n')

# Mesmo usando o seek(0) para movimentar o cursor ao início
# do arquivo, o modo 'a' de open() adiciona ao final (SEMPRE
# ao final). Com o modo 'a', não controlamos o cursor.

# Exemplo usando o modo 'r+' da função 'open()':
with open('outro.txt', 'r+') as file_rplus:
	file_rplus.write("Adicionada. \n")
	# file_rplus.seek()
	file_rplus.write("Nova linha. \n")
	file_rplus.seek(25)
	file_rplus.write("Mais uma linha.\n")




