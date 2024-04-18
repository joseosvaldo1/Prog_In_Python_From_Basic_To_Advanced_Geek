"""
# Módulos em Python e Módulo Random:

- Em Python, módulos nada mais são do que outros arquivos Python (.py).
- Módulos são úteis para deixar nossos programas mais simples e para
que possamos reutilizar códigos.

- Módulo Random => Possui várias funções para geração de números
pseudo-aleatórios.

# --------------------------------------------------

# Existem duas formas de se utilizar um módulo ou função deste:

# 1ª Forma - importando t o d o o módulo (NÃO RECOMENDADO):

import random

# OBSERVAÇÃO: Ao realizar o import de t o d o o módulo, todas as funções,
# atributos, classes e propriedades que estiverem dentro do módulo ficarão
# disponíveis (ficarão em memória). Caso você saiba quais funções irá
# utilizar deste módulo, então esta não seria a forma ideal de utilização.
# Nós veremos uma forma melhor na segunda forma.

print(random.random())

# random() => Gera um número pseudoaleatório dentro do intervalo [0,1).
# Veja que para utilizar a função random() do pacote random(), colocamos
# o nome do pacote e o nome da função contida nele separados por ponto.

# Observação: Não confunda a função random() com o pacote random. Pode
# parecer confuso, mas a função random() é apenas uma função dentro do
# módulo random.

# ---------------------------------------------------------



"""

# Existem duas formas de se utilizar um módulo ou função deste:

# 2ª Forma - importando uma função específica do módulo:
# (FORMA RECOMENDADA)
from random import random
from random import uniform
from random import randint
from random import choice
from random import shuffle


# No import acima, estamos falando basicamente o seguinte ao
# interpretador do Python: "Do módulo random, import a função
# random"

for i in range(10):
	print(f"{i}º: {random()}")

print(" ")
# Observações:
# 1) Quando importamos especificamente uma função de um módulo,
# não precisamos escrever antes o nome do módulo seguido do ponto.

# Para gerar números aleatórios entre dois valores estabelecidos,
# usaremos a função 'uniform()' do módulo random:

# uniform() => Gera um número pseudo-aleatório entre dois valores
# estabelecidos.

# Em Python, o método random.uniform(a, b) é usado para gerar um número
# aleatório pertencente a um intervalo específico [a, b), onde 'a' é o
# limite inferior e 'b' é o limite superior. Aqui está uma explicação
# mais detalhada:
#
# a: É o limite inferior do intervalo. O número retornado será igual ou
# maior que este valor, dependendo do caso.
# b: É o limite superior do intervalo. O número retornado será menor que
# este valor.

for i in range(10):
	print(f"{i}º: {uniform(5, 10)}")  # 10 não é incluído.

print(" ")
# radint() => Gera números inteiros pseudo aleatórios entre
# dois valores estabelecidos

# Gerador de import para megassena:

print("Números para aposta da megassena:")
for i in range(6):
	# print(f"{i+1}º number: {randint(1,61)}")
	print(randint(1,61), end=', ')
print(" ")
print(" ")

# choice() => Mostra um valor aleatório entre os valores
# de um iterável.

# Jogo pedra, papel, tesoura:
jogadas = ['pedra', 'papel', 'tesoura']
print(f"choice(jogadas) = {choice(jogadas)}")

print(" ")
print(f"choice('Geek University') = {choice('Geek University')}")

print(" ")

# shuffle() => Tem a função de embaralhar dados.
deck = [f"{value}{suit}" for value in
		  ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10',
		  'J', 'Q', 'K'] for suit in ['♠', '♣', '♥', '♦']]

# deck => baralho  suit => naipe da carta

print("Deck of cards before shuffling")
print(deck)
print("Shuffling the cards...")
shuffle(deck)
print("Deck of cards after shuffling")
print(deck)

deck_copy = deck[:]

# A linha deck_copy = deck[:] cria uma cópia superficial (shallow copy)
# da lista deck. Isso significa que deck_copy terá uma cópia dos elementos
# de deck, mas eles serão os mesmos objetos que estão na lista deck. Se
# os elementos da lista forem objetos mutáveis (como listas aninhadas,
# por exemplo), as alterações nesses objetos serão refletidas tanto em
# deck quanto em deck_copy.

# Nesse caso específico, onde os elementos da lista deck são strings
# (que são objetos imutáveis em Python), isso não faz muita diferença
# prática. Mas se você estivesse trabalhando com objetos mutáveis, você
# precisaria estar ciente de que a alteração de um objeto em deck_copy
# também seria refletida em deck, e vice-versa.

# Em resumo, deck_copy = deck[:] cria uma cópia superficial de deck,
# onde os elementos são os mesmos objetos, mas as listas em si são
# independentes, então adicionar, remover ou reordenar elementos em
# uma lista não afetará a outra.

print(f"deck_copy = {deck_copy}")
print("Dealing 5 cards from the deck: ")
for card in deck_copy[0:5]:
	print(card, end=' ')

print("\n")

