"""
# Escrevendo em Arquivos:
- Ao abrir um arquivo para leitura, não podemos realizar a escrita nele.
Só poderemos lê-lo. Da mesma forma, se abrirmos um arquivo para escrita,
não poderemos lê-lo, mas somente escrever no mesmo.

- Ao abrir um arquivo para escrita, o arquivo é criado no sistema
operacional.

- Para escrevermos dados em um arquivo, após abri-lo, utilizamos a
função 'write()'.Esta função recebe uma string como parâmetro. Caso
contrário, teremos um erro: TypeError.

- Abrindo um arquivo para escrita com o modo 'w', se o arquivo não
existir, ele será criado. Caso ele já exista, o anterior será
apagado e um novo será criado. Dessa forma, t o d o o conteúdo no
arquivo anterior é perdido.


# --------------------------------------------------------------

# Exemplo de escrita:
# Forma Pythonica de escrita em arquivos:

# with open('novo.txt', 'w') as file:
# 	file.write('Escrever dados em um arquivo é muito fácil.\n')
# 	file.write('Podemos colocar quantas linhas quisermos\n')
# 	file.write('Esta é a última.\n')

# --------------------------------------------------------------

# Usando a função write() novamente - arquivo novo.txt será sobrescrito:

with open('novo.txt', 'w') as file:
	file.write('Novos dados.\n')
	file.write('Outros dados - podemos colocar quantas linhas quisermos\n')
	file.write('Esta é a última.\n')

# --------------------------------------------------------------


# Exemplo_2:
# Forma tradicional de escrita em arquivos (Não Pythonica):

file = open('mais.txt', 'w')

file.write('Um texto qualquer \n')
file.write('Mais um texto.')

file.close()


"""

# Exemplo de escrita:
# Forma Pythonica de escrita em arquivos:

# with open('novo.txt', 'w') as file:
# 	file.write('Escrever dados em um arquivo é muito fácil.\n')
# 	file.write('Podemos colocar quantas linhas quisermos\n')
# 	file.write('Esta é a última.\n')

# Usando a função write() novamente - arquivo novo.txt será sobrescrito:

# with open('novo.txt', 'w') as file:
# 	file.write('Novos dados.\n')
# 	file.write('Outros dados - podemos colocar quantas linhas quisermos\n')
# 	file.write('Esta é a última.\n')

# Exemplo_2:
# Forma tradicional de escrita em arquivos (Não Pythonica):

# file = open('mais.txt', 'w')
#
# file.write('Um texto qualquer \n')
# file.write('Mais um texto.')
#
# file.close()

# Exemplo_3:

# with open('geek.txt', 'w') as file:
# 	file.write('Geek \n'*100)

# Exemplo_4:

# Recebendo dados do usuário e escrevendo em um arquivo:

with open('frutas.txt', 'w') as file:
	while True:
		fruit = input("Enter a name of fruit or type 'sair' para sair: " )
		if fruit != 'sair':
			file.write(fruit + '\n')
		else:
			break



