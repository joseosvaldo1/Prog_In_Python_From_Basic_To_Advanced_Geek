"""
# Set Comprehension:


- É uma maneira compacta de criar conjuntos (set) usando uma única linha
de código. Assim como as list comprehensions e dictionary comprehensions,
as set comprehensions oferecem uma sintaxe concisa e eficiente para
criar conjuntos de forma mais legível.

 - A sintaxe básica de uma set comprehension é semelhante à de dictionary
 comprehension, mas sem a especificação de pares chave-valor. A estrutura
 básica é a seguinte:

              {expressao for elemento in iterável}
              {expression for element in iterable}

- Aqui está um exemplo simples para ilustrar como funciona. Suponha que
você queira criar um conjunto contendo os quadrados dos números de 0 a 4:

quadrados = {x**2 for x in range(5)}
print(quadrados)

- O resultado seria:
{1, 4, 9, 16}

- Assim como nas comprehensions de lista e dicionário, você também pode
adicionar condições para filtrar os elementos incluídos no conjunto final.
Por exemplo, se você quiser apenas os quadrados dos números pares:

quadrados_pares = {x**2 for x in range(5) if x % 2 == 0}
print(quadrados_pares)

- O resultado seria:
{0, 4, 16}

- As set comprehensions são úteis quando você precisa criar conjuntos de
maneira eficiente e concisa, especialmente quando deseja aplicar
transformações ou filtrar elementos com base em condições específicas.


# --------------------------------------------------------------------


"""

# Exemplos:

# Exemplo_1:

numbers = {number for number in range(1, 7)}

print(f"numbers: {numbers}")
print(15*'-')

# Exemplo_2:

numbers_2 = {number**2 for number in range(10)}
print(f"numbers_2: {numbers_2}")
print(15*'-')

# Desafio: Faça uma alteração na estrutura acima para gerar um dicionário
# em vez de um set.

# Exemplo_3:

numbers_3 = {number: number**2 for number in range(10)}
print(f"numbers_3: {numbers_3}")
print(15*'-')

# Exemplo_4 - com String:

letters = {letter for letter in 'Geek University'}
print(f"letters: {letters}")