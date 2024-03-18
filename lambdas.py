"""
# Utilizando Lambdas:

- Conhecidas por Expressões Lambdas, ou simplesmente Lambdas, são
funções sem nomes (funções anônimas).


- Uma expressão lambda em Python é uma forma concisa de criar funções
anônimas, ou seja, funções sem um nome definido. Essas funções são úteis
quando você precisa de uma função temporária para uma operação específica
e não deseja definir uma função completa com um nome específico.

- A sintaxe básica de uma expressão lambda é:

                lambda argumentos: expressao
                lambda arguments: expression

- Aqui, "lambda" é uma palavra-chave que indica que você está criando
uma função lambda, seguida por uma lista de argumentos separados por
vírgula, seguida por dois pontos ":" e a expressão que a função lambda
retorna.

- Por exemplo, suponha que você queira criar uma função simples que
retorna o dobro de um número. Você pode fazer isso com uma expressão
lambda da seguinte maneira:

dobro = lambda x: x * 2
- Agora, dobro é uma função lambda que aceita um argumento x e retorna
o dobro desse argumento.

- Você pode então chamar essa função dobro com um valor específico:

print(dobro(5))  # Saída: 10

- As expressões lambda são frequentemente usadas em Python em situações
onde você precisa de uma função rápida e temporária, como em operações
de filtragem, mapeamento e ordenação. Elas são especialmente úteis
quando você precisa passar uma função como argumento para outra função,
como em map(), filter() e sorted(). Por exemplo:

numeros = [1, 2, 3, 4, 5]
dobro_numeros = map(lambda x: x * 2, numeros)
print(list(dobro_numeros))  # Saída: [2, 4, 6, 8, 10]

- Embora úteis, é importante usá-las com moderação, pois expressões lambda
podem tornar o código menos legível se forem muito complexas. Em casos
onde a lógica da função é mais complexa, é preferível definir uma função
regular com uma declaração 'def'.

# -------------------------------------------------------------

# Exemplo de função em Python:


def function(x):
    return 3*x + 1


print("function(x) = 3x +1")
print(f"function(4) = {function(4)}")
print(15*'-')
print(f"function(7) = {function(7)}")
print(15*'-')
print(20*'-')


# Exemplo de Expressão Lambda:


calc = lambda x: 3*x + 1

print("calc = lambda x: 3*x + 1")
print(f"calc(4) = {calc(4)}")
print(15*'-')
print(f"calc(7) = {calc(7)}")
print(15*'-')

# Podemos ter expressões lambdas com múltiplas entradas:


full_name = lambda name, surname: (name.strip().title() + " " +
   surname.strip().title())

print(full_name(" carlos alberto ", " costa silva"))
print(15*'-')
print(full_name("   FELICITY    ", "   jones    "))
print(15*'-')

# --------------------------------------------------------

# Assim como em funções em Python, nas expressões lambas podemos
# ter nenhum ou várias entradas.

love = lambda: "Como não amar Python?"
first_lambda = lambda x: 3*x +1
second_lambda = lambda x, y: (x*y)**0.5
third_lambda = lambda x, y, z: 3 / (1 / x + 1/ y + 1 / z)
# n = lambda x1, x2, x3, ..., xn: <expressão>

print(f"lamba 'love' = {love}")
print(15*'-')
print(f"first_lambda(6) = {first_lambda(6)}")
print(15*'-')
print(f"second_lambda(5, 7) = {second_lambda(5, 7):.2f}")
print(15*'-')
print(f"third_lambda(3, 6, 9) = {third_lambda(3, 6, 9):.2f}")
print(15*'-')

# Observação: Se passarmos mais argumento do que parâmetros esperados,
# obteremos um TypeError.

# Outro Exemplo:

authors = ['Issac Asimov', 'Ray Bradbury', 'Robert Heileins',
           'Arthur C. Clarke', 'Frank Hebert', 'Orson Scott Card',
           'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']

print(f"authors: {authors}")
print(15*'-')
authors.sort(key=lambda surname: surname.split(" ")[-1].lower())
print(f"authors_ordered_by_surname: {authors}")
print(15*'-')

# -----------------------------------------------------

"""

# Função Quadrática:

# f(x) = a*x**2 + b*x + c, com != 0

# Definindo a função:

def geradora_funcao_quadratica(a, b, c):
	"""
	Retorna a função: f(x) = a.x² + b.x + c,
	com a ǂ 0 e a ϵ ǀR, b ϵ ǀR e c ϵ ǀR.
	"""
	return lambda x: a*x**2 + b*x + c


teste = geradora_funcao_quadratica(a=2, b=3, c=-5)

print("teste(x) = geradora_funcao_quadratica(2, 3, - 5)")
print("teste(x) = 2.x² + 3.x - 5")
print(f"teste(0) = {teste(0)}")
print(15*'-')
print(f"teste(1) = {teste(1)}")
print(15*'-')
print(f"teste(2) = {teste(2)}")
print(15*'-')
print(15*'-')
print(f"geradora_funcao_quadratica(3, 0, 1)(2) = "
	  f"{geradora_funcao_quadratica(3, 0, 1)(2)} ")






