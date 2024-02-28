"""
# Funções Com Retorno:

# Recapitulando funções:

numbers = [1, 2, 3]
ret_pop_numbers = numbers.pop()
# pop() remove e retorna o último elemento da lista.

print(f"Retorno de pop em numbers: {ret_pop_numbers}")
ret_print_numbers = print(f"number = {numbers}")

print(f"Retorno de print em numbers = {ret_print_numbers}")

print(15*'-')

Observação:
1) Quando uma função não retorna nenhum valor, o retorno será 'None'.
2) Funções em Python que retornam valores devem retornar estes
valores com a palavra reservada 'return'.
3) Não precisamos necessariamente criar uma variável para receber o
retorno de uma função. Podemos passar a execução de uma função para
outras funções.

# Vantagens do Uso de Return em Funções no Python:

O uso de uma função com um retorno explícito em Python oferece várias
vantagens:

- Clareza e Intenção Explícita:

Um retorno explícito torna claro qual é o valor que a função está
devolvendo. Isso melhora a legibilidade do código, facilitando a
compreensão das intenções do programador.

- Reutilização de Resultados:

O valor retornado pela função pode ser armazenado em uma variável e
reutilizado em outras partes do código. Isso promove a reusabilidade
de resultados calculados ou processados pela função.

- Facilita a Depuração:

Ao utilizar retornos explícitos, é mais fácil depurar o código. Você pode
imprimir ou examinar diretamente o valor retornado pela função para
entender o que está acontecendo.

- Integração com Outras Funções e Expressões:

Funções com retornos explícitos podem ser facilmente integradas em
expressões ou usadas como parte de chamadas de outras funções, o
que torna o código mais flexível e modular.

- Compatibilidade com Estruturas de Controle:

Funções com retornos explícitos podem ser usadas facilmente em
estruturas de controle de fluxo, como condicionais e loops, onde
o valor retornado pode influenciar o comportamento do programa.

- Testabilidade:

Ao ter um retorno explícito, torna-se mais fácil escrever testes para
a função. Os testes podem verificar se a função retorna os resultados
esperados em diferentes situações, contribuindo para a robustez do
código.

- Conformidade com Boas Práticas:

Em muitos casos, seguir a prática de ter retornos explícitos é uma
convenção e uma boa prática de programação em Python. Isso alinha o
código com as diretrizes da comunidade e facilita a colaboração em
projetos.
Embora o uso de funções sem retorno (ou com um retorno implícito
None) seja permitido em Python, adotar a prática de retornos
explícitos contribui para um código mais legível, modular e fácil
de manter.


# ------------------------------------------------------

# Exemplo de função:

# def quadrado_de_sete():
# 	print(7**2)

# ret = quadrado_de_sete()
#
# print (f"Retorno = {ret}")
# print(15*'-')

# Vamos refatorar a função quadrado_de_sete para que
# ela retorne algo:

def quadrado_de_sete():
	return 7**2

# Criamos uma variável para receber o retorno da função acima.
ret = quadrado_de_sete()

print(f"Retorno de quadrado: {ret}")
print(15*'-')
print(f"Retorno de quadrado + 1: {quadrado_de_sete() + 1}")
print(15*'-')

# Refatorando a função say_hi():
def say_hi():
	return 'Hi'

print(say_hi())
print(15*'-')

-----------------------------------------------------------------
Observações sobre a palavra reservada 'return':

1) Ela finaliza a função, ou seja, ela sai da execução da função.
2) Podemos ter, em uma função diferentes, retornos.
3) Podemos em uma função podemos retornar qualquer tipo de dado e
até mesmo múltiplos valores.

------------------------------------------------------------------

# Exemplo_1 - função finalizando a função:

def say_hi():
	print("Estou sendo executado ANTES do retorno!")
	return 'Hi'
	print("Estou sendo executado após o retorno!") # => Nunca será executado


print(say_hi())

# Exemplo_2 - funções com diferentes retornos:

def nova_funcao():
	variavel = True
	if variavel:
		return 4
	elif variavel == None:
		return 3.2
	else:
		return 'b'


print(nova_funcao())
print(15*'-')

# Exemplo_3 - funções com com múltiplos valores de retorno:


def outra_funcao():
	return 2, 3, 4, 5

num1, num2, num3, num4 = outra_funcao()

print(num1, num2, num3, num4)
print(15*'-')
print(f"outra_funcao = {outra_funcao()}")
print(f"type(outra_funcao) = {type(outra_funcao())}")

# Vamos criar uma função que simule o lançamento de uma moeda:

from random import random

def joga_moeda():
	# Gera um número pseudo randômico entre 0 e 1:
	valor = random()
	if valor > 0.5:
		resultado = 'Cara'
	else:
		resultado = 'Coroa'

	return "{:.2f} - {}".format(valor, resultado)
print(joga_moeda())

print(15*'-')


def flip_coin():
	# Generates a pseudo-random number between 0 and 1:
	value = random()
	if value > 0.5:
		result = 'Heads'
	else:
		result = 'Tails'

	return "{:.2f} - {}".format(value, result)


print(flip_coin())

print(15*'-')


"""


# Erros comuns na utilização do return (codificação desnecessária):


def eh_impar():
	numero = 6
	if numero % 2 != 0:
		return True
	return False

print(eh_impar())



