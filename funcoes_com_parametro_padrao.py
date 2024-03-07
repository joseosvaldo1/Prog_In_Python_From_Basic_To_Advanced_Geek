"""
# Funcçoes com Parâmetro Padrão:

- Funções em que a passagem de parâmetro é opicional.

# -------------------------------------------------------

# Exemplo de função em que a passagem de parâmetro é opicional:
print("Geek University")
print()

# Exemplo de função em que a passagem de parâmetro é obrigatório:
def quadrado(number):
	return number ** 2
print(quadrado(3)) # => 9
# print(quadrado()) #=> TypeError: quadrado() missing
# 1 required positional argument: 'number'

# -------------------------------------------------------

def exponencial(base, exponente=2):
	return base ** exponente


print(f"exponencial(base=2, exponente=3) = {exponencial(base=2, exponente=3)}")
# => 2*2*2 = 2**3 = 8

print(f"exponencial(base=3, exponente=2) = {exponencial(base=3, exponente=2)}")
# => 3*3 = 3**2 = 9

print(15*'-')

print(f"exponencial(3) = {exponencial(3)}") # Eleva a base ao quadrado por padrão.
print(f"(exponencial(3, 5) = {exponencial(3, 5)}")

print(15*'-')

# Com a função 'exponencial()' refatorada usando um valor padrão:
# 1) Se o usuário passar somente um 1 argumento, este será atribuído ao
# parâmetro 'base' e será calculado o quadrado do mesmo.

# 2) Se o usuários passar 2 argumentos, o primeiro será atribuído ao
# parâmetro 'base' e o segundo ao parâmetro 'exponente'. Então, será
# calculada a exponenciação.

# Observações:
# 1) Quando na definição de uma função em Python atribuímos
# um valor para um dos parâmetros, esse parâmetro se torna opicional
# e o valor atribuído a ele na definição será uma valor padrão.

# 2) Em funções Python, os parâmetros com valores padrões (deafult)
DEVEM sempre estar ao final da declaração.

# ERRO:
# def teste(numero=2, potencia):
# 	return numero**potencia
#
# print(teste(6))

# Saída do Erro: SyntaxError: parameter without a default follows
# parameter with a default (parâmetro sem padrão segue parâmetro
# com padrão)


def teste(potencia, numero=2):
	return numero**potencia

print(teste(6))

# -------------------------------------------------------

# Outros Exemplos:

# def soma(numero1, numero2):
# 	return numero1 + numero2


# print(f"soma(4,3) = {soma(4,3)}")
# print(f"soma(4) = {soma(4)}") # TyeError
# print(f"soma(3) = {soma(3)}") # TyeError
# TypeError: soma() missing 1 required positional
# argument: 'numero2'


# Refatorand a função 'soma()':
def soma(numero1=0, numero2=0):
	return numero1 + numero2


print(f"soma(4,3) = {soma(4,3)}")
print(f"soma(4) = {soma(4)}")
print(f"soma(3) = {soma(3)}")

# -------------------------------------------------------

# Exemplo Mais Complexo:

def mostra_informacao(nome="Geek", instrutor=False):
	if nome == "Geek" and instrutor:
		return "Bem vindo instrutor Geek"
	elif nome == "Geek":
		return "Eu pensei que você fosse o instrutor"
	return f"Olá, {nome}"


print(mostra_informacao())
print(15*'-')
print(mostra_informacao(instrutor=True))
print(15*'-')
print(mostra_informacao(True))
print(15*'-')
print(mostra_informacao('Ozzy'))
print(15*'-')
print(mostra_informacao(nome='Stephany'))
print(15*'-')

# -------------------------------------------------------

# Por que utilizar funções com parâmetro padrão:
1) Permite ser mais flexível nas funções;
2) Evita erros com parâmetros incorretos;
3) Permite-nos trabalhar com exemplos mais legíveis de códigos.


# Quais tipos de dados podemos usar como valores default
para parâmetos:
- Podemos usar todo tipo de dado em Python: números, strings, funções,
listas, tuplas, dicionários, etc.

# -------------------------------------------------------

# Exemplos de uso de funções como parâmetros:

def soma(num1, num2):
	return num1 + num2

def mat(num1, num2, function = soma):
	return function(num1, num2)

def subtracao(num1, num2):
	return num1 - num2

print(f"mat(2, 3) = {mat(2,3)}")
print(15*'-')
print(f"mat(2, 2, subtracao) = {mat(2,2, subtracao)}")
print(15*'-')

# -------------------------------------------------------

# Escopo - Evitar problemas e confusões:

# - Variáveis globais: São reconhecidas em todos os locais do código.

# - Variáveis locais: Só são reconhcidas dentro bloco de código onde
foram declaradas.


instrutor = 'Geek'  # => Variável Global

def diz_oi():
	instrutor = "Python"  # => Variável local
	return f"Oi, {instrutor}!"

print(diz_oi()) # => Oi, Python!


# Observação: Se tiver uma variável local com o mesmo nome de uma
# variável global, a local terá a preferência.

def diz_oi():
	prof = 'Geek' # => Variável Local
	return f"Oi, {prof}"


print(diz_oi())
# print(prof) # => NameError: name 'prof' is not defined

# ATENÇÃO com variáveis globais: Se puder, evite-as!


# -------------------------------------------------------

total = 0

def incrementa():
	total = total +1
	return total


print(f"total = {total}")
# print(f"incrementa = {incrementa()}")
# UnboundLocalError: cannot access local variable
# 'total' where it is not associated with a value

# Traduzindo a mensagem de erro:
# UnboundLocalError: não é possível acessar a variável
# local 'total' onde ela não está associada a um valor

# Explicando melhor:
# A variável 'total' local está sendo utilizada para
# processamento sem ter sido inicializada

total = 0

def incrementa():
	global total    # -> Indicamos o uso da variável global 'total'
	total = total + 1
	return total


print(f"total = {total}")
print(f"incrementa() - 1ª chamada = {incrementa()}")
print(f"incrementa() - 2ª chamada = {incrementa()}")
print(f"incrementa() - 3ª chamada = {incrementa()}")
print(15*'-')

# -------------------------------------------------------

"""

# Podemos ter funções sendo declaradas dentro de outras funções
# e também têm uma forma especial de escopo de variáveis:

def fora():
	contador = 0

	def dentro():
		nonlocal contador  # 'nonlocal' indica que 'contador'
						   # está na funcao anterior
		contador = contador + 1
		return contador
	return dentro()


print(f"1ª chamada de 'fora()' = {fora()}")
print(f"2ª chamada de 'fora()' = {fora()}")
print(f"3ª chamada de 'fora()' = {fora()}")
print(15*'-')
# print(f'dentro() = {dentro()}') # => NameError: name 'dentro' is
# not defined