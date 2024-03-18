"""
# Map:

- Em Python, "maps" refere-se a uma função embutida que permite aplicar
uma função a cada item de um ou mais iteráveis (listas, tuplas, etc.) e
retorna um iterador que produz os resultados dessas aplicações.

- A sintaxe básica da função map é a seguinte:

     map(função, iterável1, iterável2, ...)

* função: é a função que você deseja aplicar a cada item do iterável.
* iterável1, iterável2, etc.: são os iteráveis que contêm os elementos
aos quais a função será aplicada.

- Por exemplo, vamos supor que temos uma lista de números e queremos
calcular o quadrado de cada número:

numeros = [1, 2, 3, 4, 5]
quadrados = map(lambda x: x ** 2, numeros)

- Neste exemplo, lambda x: x ** 2 é uma função lambda que calcula o
quadrado de um número. Passamos esta função juntamente com a lista de
números para a função map. O resultado será um iterador que produz os
quadrados de cada número quando iterado.

- Para visualizar os resultados, podemos convertê-los em uma lista:

quadrados = list(quadrados)
print(quadrados)  # Saída: [1, 4, 9, 16, 25]

- O uso da função map é útil quando você precisa aplicar uma operação
simples a todos os elementos de um ou mais iteráveis sem a necessidade
de escrever um loop explícito. No entanto, deve-se ter cuidado ao usar
map com funções que possam ter efeitos colaterais, pois isso pode tornar
o código menos legível. Em muitos casos, uma compreensão de lista ou um
loop explícito podem ser mais claros.

# ------------------------------------------------------

- Com o 'map', fazemos mapeamento de valores para função.

# Exemplo_1:

import math

def circle_area(r):
    '''Calcula a área de um círculo de raio 'r'.'''
    return math.pi * (r**2)


print(f"circle_area(2) = {circle_area(2):.2f}")
print(15*'-')
print(f"circle_area(5.3) = {circle_area(5.3):.2f}")
print(15*'-')
print(15*'-')

# Para uma lista de medidas de raios de círculos:

radius_list = [2, 5, 7.1, 0.3, 10, 44]

# Forma 1: Usando um loop 'for':
# areas_list = []
#
# for r in radius_list:
#     circle_area(r)
#     areas_list.append(circle_area(r))
#
# print(f"areas_list = {areas_list}")
#
# print(30*'-')
# print(" ")

# Forma 2: Usando o 'map':

# 'map' é uma função que recebe, no mínimo, dois parâmetros:
# o primeiro é uma função e o segundo um iterável,
# podendo ter mais de um iterável, retornando um 'map object'.

areas = map(circle_area, radius_list)
print(f'areas = {areas}')
print(15*'-')
print(f"type(areas) = {type(areas)}")
print(15*'-')
areas_list = list(areas)
print(f"areas_list = {areas_list}")
print(15*'-')
print(f"areas_tuple = {tuple(areas_list)}")
print(15*'-')
print(f"areas_set = {set(areas_list)}")
print(15*'-')

# Forma 3: Usando Map e Lambda:

areas = map(lambda r: math.pi*(r**2), radius_list)
print(f"list(areas) = {list(areas)}")
print(15*'-')

# Observações:
# 1) Após utilizar a função map(), depois da primeira
# utilização do resultado, ele será zerado.  Isso acontece porque
# os iteradores em Python mantêm um estado interno e avançam para
# o próximo item a cada chamada. Uma vez que o iterador foi
# totalmente consumido, ele não tem mais itens para fornecer.
# 2) Se você quiser usar os resultados do map() mais de uma vez,
# você pode converter o iterador em uma lista. Isso irá armazenar
# os resultados em uma lista que pode ser usada várias vezes. No
# entanto, tenha em mente que converter o iterador em uma lista pode
# consumir mais memória, especialmente se a sequência for grande.
# Portanto, é uma troca entre economia de memória e reutilização dos
# resultados.

# --------------------------------------------------------------

"""

# Para fixar - Map:

# Temos os dados em um iterável - dados: a1, a2, ..., an;
# Tem uma função - função: f:f(x);
# Utilizamos a função 'map(f, iterável)', onde map() irá mapear
# cada elemento dos dados do iterável e aplicar a função a cada
# um dos dados.

# O map object: f(a1), f(a2), ..., f(an).

# Mais um Exemplo:

# Exemplo_2:

# Cities = Cidade e temperatura em graus Celsius

cities_tempratures_c = [('Berlin', 29), ('Cairo', 36), ('Buenos Aires', 19),
                        ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28),
                        ('Londres', 22)]

print(f"cities_tempratures_c  = {cities_tempratures_c }")

# Precisamos transformas em graus fareheit:

# Tf = (9/5).Tc + 32

celsius_para_fahrenheit = lambda data: (data[0], (9/5)*data[1] + 32)

cities_tempratures_f = list(map(celsius_para_fahrenheit, cities_tempratures_c ))

print(f"cities_tempratures_f = {cities_tempratures_f} ")


