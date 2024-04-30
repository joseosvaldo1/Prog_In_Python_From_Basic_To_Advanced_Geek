"""
# Sistemas de Arquivos - Manipulação:


# ----------------------------------------------------------------

import os

# Descobrindo se um arquivo ou diretório existe:


# Para arquivos:
print(f"os.path.exists('arquivo.txt') = {os.path.exists('arquivo.txt')}")
# Saída - Output => False.

print(15*'-')
print(f"os.path.exists('frutas.txt') = {os.path.exists('frutas.txt')}")
# Saída - Output => True.
print(15*'-')


# Para diretórios:
# Caminhos relativos:
print(f"os.path.exists('geek') = {os.path.exists('geek')}")
# Saída - output: os.path.exists('geek') = True
print(15*'-')

print(f"os.path.exists('geek/university') = "
	  f"{os.path.exists('geek/university')}")
# Saída - output: os.path.exists('geek/university') = True
print(15*'-')

print(f"os.path.exists('outro') = {os.path.exists('outro')}")
# Saída - output: os.path.exists('outro') = False
print(15*'-')

# Caminhos absolutos:
print(f"os.path.exists('/home/jose') = {os.path.exists('/home/jose')}")
# Saída - output: os.path.exists('/home/jose') = True
print(15*'-')

print(f"os.path.exists('/home/jose/outra_pasta') = "
	  f"{os.path.exists('/home/jose/outra_pasta')}")
# Saída - output: os.path.exists('/home/jose/outra_pasta') = False
print(15*'-')



# ----------------------------------------------------------------

# Forma 1:
# open('arquivo-test.txt', 'w').close()

# Forma 2:
# open('arquivo-test2.txt', 'a').close()

# Forma 3:

# with open('arquivo-teste3.txt', 'w') as arquivo_3:
# 	pass



# ----------------------------------------------------------------

# Criando arquivos:
os.mknod('arquivo-teste4.txt')
os.mknod('/home/jose/PycharmProjects/guppe/guppe/' +
		 'Prog_In_Python_From_Basic_To_Advanced_Geek/' +
		 'university.txt')

# Observações:
# 1) Se estiver utilizando o Python no MacOS, poderá ocorrer
# um erro: PermissionError.
# 2) Criando um arquivo com a função 'mknod()', se o arquivos
# já existir, teremos o seguinte erro: FileExistsError.



# ----------------------------------------------------------------

# Criando diretórios:

# Caminho relativo:
# os.mkdir('templates')

# Caminho absoluto:
# os.mkdir('/home/jose/PycharmProjects/guppe/guppe' +
# 		 '/Prog_In_Python_From_Basic_To_Advanced_Geek/' +
# 		 'templates_2')

# Exceção de diretório onde se precisa de permissão:
# os.mkdir('/etc/pasta')

# Observações:
# 1) A função mkdir() cria um diretório caso o mesmo não
# exista. Caso exista, teremos um erro: FileExistsError.
# 2) Se não tivermos permissão para criar um diretório,
# teremos um erro: PessionError.

# Criando diretórios com subdiretórios - usando a
# função 'makedirs()':
# os.makedirs('templates/geek/university')
os.makedirs('templates_2/novo_2/outro_2', exist_ok=True)

# Observações:
# 1) Se a estrutura de diretórios já existir,
# teremos um erro: FileExistsError.
# 2) Podemos usar o parâmetro 'exists_ok=True' (por padrão,
# esse parâmetro é False), para ignorar o erro do FileExistsError.


# ----------------------------------------------------------------


# Renomear arquivos e diretórios:

# Diretórios:
# os.rename('templates_2', 'geek_2')
# os.rename('geek_2/novo_2', 'geek_2/novo_II')

# Observações:
# 1) Se o diretório não existir, teremos um erro:
# FileNotFoundError
# 2) Se o diretório que queremos renomear não estiver vazio,
# teremos um erro: OSError.

# Arquivos:
os.rename('geek_2/novo_II/outro_2/teste_2.txt',
		  'geek_2/novo_II/outro_2/teste_II.txt')

# Observação: Deve-se manter a estrutura de diretório anterior
# em que se encontra o arquivo a ser renomeado quando usar a
# função os.rename. No exemplo acima, mantivemos:
# geek_2/novo_II/outro_2/

os.rename('frutas.txt', 'cesta_de_frutas.txt')

# ----------------------------------------------------------------


# Deletando arquivos:

os.remove('geek.txt')

# Observações:
# 1) ATENÇÃO: Tome cuidado com os comando de deleção do Python. Ao
# deletarmos um arquivo ou diretório, eles não vão para a lixeira.
# Eles somem de forma definitiva.
# 2) Se você estiver no windows e o arquivo que você for
# deletar, você estiver em uso, você terá um erro: PermissionError
# 3) Caso o arquivo não exista, ao usar o os.remove() teremos
# um erro: FileNotFoundError.
# 4) Se for tentarmos remover um diretório no lugar de um arquivo
# usando os.remove() teremos um erro: IsNotDirectoryError.


# ----------------------------------------------------------------

# Removendo diretórios vazios - os.rmdir():
# os.rmdir('templates')  # => OSError: [Errno 39] Directory
# not empty: 'templates'

# os.rmdir('templates42')  # => FileNotFoundError: [Errno 2]
# No such file or directory: 'templates42'

os.rmdir('templates')


# Observações:
# 1) Se o diretório tiver qualquer conteúdo, teremos um erro: OSError;
# 2) Se o diretório a ser deletado não existir, termos um erro:
# FileNotFoundError.

# ----------------------------------------------------------------

# Removendo vários arquivos de uma vez usando um laço 'for':
for file in os.scandir('geek_2'):
	print(f"File: {file.name}")
	if file.is_file():
		os.remove(file.path)

# ----------------------------------------------------------------

# Podemos remover uma árvore de diretórios vazios:

os.removedirs('geek_2/Outro/outro subdiretório')

# Observações:
# 1) Se algum dos diretórios da árvore de diretórios a ser
# deletada usando a função os.removedirs() contiver arquivos
# ou outros subdiretórios, o processo irá parar.


# ----------------------------------------------------------------

from send2trash import send2trash

# Usando o os.remove():
# os.remove('cesta_de_frutas1.txt')   # Não irá para a lixeira.
# send2trash('cesta_de_frutas2.txt')  # Irá para a lixeira.
send2trash('teste')


# Observações:
# 1) Se o arquivo a ser enviado para a lixeira usando o
# método send2trash() não existir, teremos um erro: OSError.
# 2) a função 'send2trash()' envia tanto arquivos quanto
# diretórios para a lixeira.


# ----------------------------------------------------------------

import tempfile

# Trabalhando com arquivos e diretórios temporários:

# Criando um diretório temporário:
with tempfile.TemporaryDirectory() as tmp:
	print(f"I created a temporary directory em: {tmp}")
	with open(os.path.join(tmp,'temporary_file.txt'), 'w') as file:
		file.write('Geek University!\n')
		input()

# No código acima estamos criando um diretório temporário,
# abrindo o mesmo e, dentro dele, criando um arquivo para
# escrevermos nele. No final, usamos a função input() para
# deixar o arquivos e o diretório temporários disponíveis
# dentro dos blocos with.

# Observação: Possivelmente o código acima não irá funcionar
# se estiver utilizando o windows, pois o mesmo trabalha de
# forma diferente com arquivos e diretórios temporários.

# Criando um arquivo temporário:

with tempfile.TemporaryFile() as tmp:
	tmp.write(b"Geek University.\n")
	tmp.seek(0)
	print(tmp.read())

# Observação: Em arquivos temporários, só conseguimos escrever
# bits. Por isso, tivemos que utilizar um 'b' antes da string
# passada em tmp.write().


# Criando um arquivo temporário sem usar o 'with':
file = tempfile.TemporaryFile()
file.write(b"Geek University.\n")
file.seek(0)
print(f"file.read() = {file.read()}")
file.close()

"""

import os
import tempfile























