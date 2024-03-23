"""
# Reduce:

- A função 'reduce()' deixou de ser uma função integrada a partir do
Python 3.0. Antes do Python 3.0, reduce() era uma função integrada
no módulo functools. No entanto, devido a preocupações com a legibilidade
e com o fato de que muitas vezes uma compreensão de lista ou um loop for
era mais claro, a função reduce() foi removida do escopo padrão e movida
para o módulo functools. Isso foi feito para enfatizar que a programação
funcional, embora suportada em Python, não é a abordagem preferida na
linguagem.

- Para usar a função reduce(), devemos importar inicialmente o módulo
'functools'

- Guido van Rossum: "Utilize a função 'reduce()' se você realmente
precisar dela. Em t o d o caso, um loop for é mais legível."

- Assim como as funçeõs map() e filter(), a função 'reduce()' recebe
dois parâmetros - uma função e um iterável.

          reduce(função, iterável)


# Para entender o reduce:

- Imagine que você tem uma coleção de dados:

data = [a1, a2, a3, ..., an]

- E você tem uma função que recebe dois parâmetros:

def function(x,y):
    return x*y

- A função reduce funciona da seguinte forma:
* Passo_1: res1 = f(a1, a2) # => Aplica a função f aos dois primeiros
elementos da coleção e guarda o resultado em res1;
* Passo_2: res2 = f(res1, a3) # Aplica a função f passando o resultado
do Passo_1 e guarda o resultado em res2;
* Passo_3: res3 = f(res3, a4) # Aplica a função f passando o resultado
do Passo_2 e guarda o resultado em res3;
    .
    .
    .
* Passo_n: resn = f(resnmenosum,an) # Aplica a função f passando o
resultado do Passo_(n-1) e guarda o resultado em resn;

- Ou seja, em cada passo, reduce() aplica a função f passando como
primeiro argumento o resultado da aplicação anterior. No final, ela
irá retornar o resultado final.

- Alternativamente, poderíamos ver a função reduce como:
função(função(...função(a1,a2), a3, a4,...), an)
f(f(...f(a1,a2), a3, a4,...), an)


"""

from functools import reduce

# Como a reduce() funciona na prática:
# Exemplos:


print("Utilizando a função reduce(): ")

# Vamos usar a função reduce() para multiplicar
# todos os elementos de uma lista de números

data = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

# Para usar a função reduce, precisamos de uma função
# que receba dois parâmetros:

mult = lambda x, y: x*y

result = reduce(mult, data)

print(f"result = {result}")

print(15*'-')

print("Utilizando um loop for no lugar da reduce(): ")

res = 1

for n in data:
    res = res * n

print(f"result = {res}")

print(15*'-')



