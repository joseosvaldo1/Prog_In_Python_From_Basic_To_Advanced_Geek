"""
# Debugando com PDB:
PDB - Python Debugger.
BUG - inseto - problema de código.
- Debugar: Debugar em programação é o processo de identificar e
corrigir erros ou bugs em um programa de computador. Isso envolve
rastrear e analisar o código para encontrar onde ocorrem os problemas
e, em seguida, fazer as correções necessárias para que o programa
funcione conforme o esperado.

- Na atividade de debugar É sempre importante quais os valores de uma
variável em um determinado ponto de execução ou como determinados dados
estão chegando em uma função.

# --------------------------------------------------------------

# OBSERVAÇÃO: A utilização da função 'print()' é uma prática
# de debugação é ruim.
def dividir(a, b):
	print(f"a = {a}, b = {b}")
	try:
		return float(a) / float(b)
	except (ValueError, ZeroDivisionError) as err:
		return f"An unexpected error occurred: {err}"


print(f"dividir(4,7) = {dividir(4, 7) :.2f}")

# ---------------------------------------------------------------
- Step Into (Passo Dentro): Com o "Step Into", você pode entrar em
chamadas de função para depurar linha por linha dentro delas. Isso é
útil para entender o funcionamento interno de funções específicas
(tecla de atalho: F7).

- Step Over (Passo Sobre): O "Step Over" permite que você avance para
a próxima linha de código sem entrar em detalhes de chamadas de função.
É útil quando você quer apenas avançar na execução do código atual (tecla
de atalho: F8).

- Step Out (Passo para Fora): O "Step Out" é usado para sair da função
atual em que você está depurando e retornar à função chamadora. Isso é
útil quando você quer voltar ao contexto anterior (tecla de atalho: shift
+ F8).

- Resume Program (Continuar Programa): O "Resume Program" permite que você
continue a execução do programa normalmente após pausar a depuração. Isso é
útil quando você já fez as verificações necessárias e deseja continuar a
execução sem depurar linha por linha (tecla de atalho: F9).

- Stop (Parar): O "Stop" termina a execução do programa e encerra o
processo de depuração. Isso é útil quando você deseja interromper a
execução do programa completamente (tecla de atalho: ctrl +F2).

- Rerun (Executar Novamente): A opção "Rerun" permite que você reinicie a
execução do programa a partir do início. Isso é útil quando você fez
alterações no código e deseja executar o programa novamente para verificar
o comportamento (tecla de atalho: ctrl + F5)

# --------------------------------------------------------------

# Existem formas mais profissionais de se fazer o 'debug',
# utilizando o debugger:

# Em Python, podemos fazer isto em diferentes IDE, como o
# PyCharm ou utilizando o Python Debugger - PDB:

# Exemplo com o PyCharm:

def dividir(a, b):
	try:
		return float(a) / float(b)
	except (ValueError, ZeroDivisionError) as err:
		return f"An unexpected error occurred: {err}"


print(f"dividir(4,7) = {dividir(4, 7) :.2f}")

# -----------------------------------------------------------
# Exemplo com o PDB - Python Debugger - Exemplo_1:
# Para utilizarmos o Python Debugger, precisamos importar a biblioteca pdb
# e então utilizar a função 'set_trace()':

# Comandos básicos do PDB:
# l => listar onde estamos no código;
# n => próxima linha;
# p => imprime variável;
# c => continua a execução e finaliza o debug.

name = 'Angelina'
surname = 'Jolie'
pdb.set_trace()
full_name = name + ' ' + surname
course = 'Essential Python Programming'

final = name + ' takes the course of ' + course
print(final)

# --------------------------------------------------

# Existem formas mais profissionais de se fazer o 'debug',
# utilizando o debugger:

# Em Python, podemos fazer isto em diferentes IDE, como o
# PyCharm ou utilizando o Python Debugger - PDB:


# Exemplo com o PDB - Python Debugger - Exemplo_2:
# Para utilizarmos o Python Debugger, precisamos importar a biblioteca pdb
# e então utilizar a função 'set_trace()':

# Comandos básicos do PDB:
# l => listar onde estamos no código;
# n => próxima linha;
# p => imprime variável;
# c => continua a execução e finaliza o debug.

name = 'Angelina'
surname = 'Jolie'

# import pdb; pdb.set_trace()  # => importamos aqui para excluir depois.
breakpoint()  # => Função integrada a partir da versão Python 3.7.
full_name = name + ' ' + surname
course = 'Essential Python Programming'

final = name + ' takes the course of ' + course
print(final)

# Por que utilizar esse formato de debug?
# O debug é utilizado durante o desenvolvimento. Costumamos realizar
# todos os import de bibliotecas no início do arquivo. Em vez de
# colocarmos o import o pdb no início do arquivo, colocamos somente
# onde iremos debugar e, ao finalizar, já fazemos a remoção.

# Observação: A partir da versão 3.7 do Python, não é mais necessário
# importar a biblioteca 'pdb', pois o comando de debug foi incorporado
# como função built-in (função integrada chamada breakpoint()).

# ----------------------------------------------------------



"""


# Cuidado com conflitos entre nomes de variáveis e comandos do pdb:

def sum(l, n, p, c):
	breakpoint()
	return l + n + p + c


print(sum(1, 3, 5, 7))


# Como os nomes das variáveis são os mesmos dos comandos do 'pdb',
# devemos utilizar o comando 'p' - print - para imprimir as
# variáveis, ou seja, p nome_da_variável.

# Não colocar nomes não representativos em variáveis. Sempre
# optar por nomes significativos.

