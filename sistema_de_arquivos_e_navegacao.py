"""
# Sistema de Arquivos e Navegação:

- Para fazer uso de manipulação de arquivos do sistema operacional,
precisamos importar e fazer uso do módulo 'os';
- os => Operating System => Sistema Operacional;

# ----------------------------------------------------------

# Fazer o import dos módulo 'os' e 'sys':

import os
import sys

# getcwd() => Get the current directory
# getcwd() => Retora o caminho absoluto do diretório atual.

cwd = os.getcwd()

print(f"Current Directory: {cwd}")
print(15*'-')
# Saída - output: Current Directory: /home/jose/PycharmProjects/guppe
# /guppe/Prog_In_Python_From_Basic_To_Advanced_Geek

# Para mudarmos de diretório, podemos usar o método 'chdir()':
os.chdir("..")
cwd = os.getcwd()
print(f"Current Directory after os.chdir('..'): {cwd}")
# Saída - output: Current Directory: /home/jose/PycharmProjects/guppe
# /guppe
print(15*'-')

# ----------------------------------------------------------

# Podemos checar se um caminho é relativo ou absoluto:

print(f"os.path.isabs('/home/jose') = {os.path.isabs('/home/jose')}")
# Saída - output => True
print(15*'-')

print(f"os.path.isabs('home/jose') = {os.path.isabs('home/jose')}")
# Saída - output => False
print(15*'-')

# Observação para usuários windows: Se você estiver usando um computador
# com o sistema operacional windows, terá que ter cuidados ao verificar
# diretórios.
# Exemplo: print(os.path.isabs("C:\\Users\\username"))


# ----------------------------------------------------------


# Podem identificar o sistema operacional com o módulo 'os'
# usando o atributo 'name':

print(f"os.name = {os.name}")  # => posix (Linux/Mac) ou nt (windows)
print(15*'-')

# Podemo obter mais detalhes do sistema operacional:

print(f"os.uname() = {os.uname()}")
# Saída - output: os.uname() = posix.uname_result(sysname='Linux',
# nodename='jose', release='6.5.0-28-generic', version='#29~22.04.1-Ubuntu
# SMP PREEMPT_DYNAMIC Thu Apr  4 14:39:20 UTC 2', machine='x86_64')
print(15*'-')

print(f"sys.platform = {sys.platform}")  # => sys.platform = linux
print(15*'-')



# ----------------------------------------------------------

# Moovendo para o diretório home:
os.chdir("/home/jose")

# Mostrando o diretório atual:
print(f"os.getcwd() BEFORE = {os.getcwd()}")  # => /home/jose

# Criando o diretório geek em /home/jose:
os.makedirs("/home/jose/geek/university", exist_ok=True)

result = os.path.join(os.getcwd(), 'geek', 'university')
os.chdir(result)

print(f"os.getcwd() AFTER = {os.getcwd()}")

# Observação: Observe que o método os.path.join() recebe no mínimo
# dois parâmetros sendo o primeiro o diretório atural e o segundo,
# o que será juntado ao atual.

# -----------------------------------------------------------------


# Podemos listar os arquivos e os diretórios usando
# o método 'listdir()':

cwd = os.getcwd()
print(f"Current Directory = {cwd}")

# Usando método listdir() em cwd:
print(f"os.listdir(cwd) = {os.listdir(cwd)}")
print(f"len(os.listdir(cwd)) = {len(os.listdir())}")
print(15*'-')
print(f"os,list('/etc') = {os.listdir('/etc')}")
print(f"len(os.listdir('/etc')) = {len(os.listdir('/etc'))}")


# -----------------------------------------------------------------


"""


# Fazer o iport do módulo 'os':

import os
import sys

# Podemos listar os arquivos e os diretórios com mais
# detalhes usando o método 'scandir()':

print(f"os.scandir('/etc') = {os.scandir('/etc')}")
# Saída - Output: <posix.ScandirIterator object at 0x7c83a4f7e9c0>
print(15*'-')

# transformando o iterator anterior numa lista:

scanner = os.scandir('/etc')
files = list(scanner)

print(f"files = {files}")
print(15*'-')
print(f"files[0] = {files[0]}")
print(f"files[0].name = {files[0].name}")  		 # => Nome do arquivo
print(f"files[0].path = {files[0].path}")		 # => Caminho do arquivo
print(f"files[0].inode() = {files[0].inode()}")  # => Inode do arquivo
print(f"files[0].is_dir() = {files[0].is_dir()}")
# => É um diretório => True
print(f"files[0].is_file() = {files[0].is_file()}")
# => É um arquivo => False
print(f"files[0].is_symlink() = {files[0].is_symlink()}")
# => É um link simbólico => False
print(f"files[0].stat() = {files[0].stat()}")  # => Estatísticas do arquivo.

# Observação: inode ) é um inteiro que identifica exclusivamente um
# arquivo ou diretório no sistema de arquivos.

# Observação: Quando usamos a função 'scandir()', nós precisamos
# fechá-la assim como fazemos quando abrimos arquivos.

scanner.close()
