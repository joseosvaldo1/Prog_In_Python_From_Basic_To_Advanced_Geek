"""
# StringIO:


- Para ler ou escrever dados em um arquivo do sistema operacional,
o software precisa ter permissão:
* Permissão de Leitura => para ler o arquivo;
* Permissão de Escrita => para escrever o arquivo.

- stringIO => Utilizado para ler e escrever arquivos em memória.

"""

# Primeiro, devemos importar o módulo stringIO:
from io import StringIO

mesage = "This is just an ordinary string."

# Podemos criar um arquivo em memória já com uma string inserida
# ou mesmo vazio para inserirmos texto depois.

file = StringIO(mesage)  # Equivalente a file open('arquivo.txt', 'w')

# Agora com o arquivo em memória podemos aplicar tudo o que
# aprendemos sobre arquivos (abrir, escrever, etc.):
print(f"file.read() = {file.read()}")

# Escrevendo outro texto:
file.write(" Other text.")

# Podemos inclurive movimentar o curso e fazer a leitura
# novamente:
file.seek(0)

print(f"file.read() AFTER seek(0) = {file.read()}")