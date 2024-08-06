"""
# Novos Recursos em Python:

- Funções Matemáticas e Estatísticas:

- Matemática:

* math.prod => Retorna o produto de um container numérico.

from math import prod

numbers_v1 = [2, 3, 6, 8]
numbers_v2 = (2, 3, 6, 8)
numbers_v3 = {2, 3, 6, 8}

print(f"{prod(numbers_v1) = }")  # => prod(numbers_v1) = 288
print(15*'-')

print(f"{prod(numbers_v2) = }")  # => prod(numbers_v2) = 288
print(15*'-')

print(f"{prod(numbers_v3) = }")  # => prod(numbers_v3) = 288
print(15*'-')

# -------------------------------------------------------------

* math.isqrt => calcula a raiz quadrada inteira de um número não negativo.
Isso significa que ele retorna o maior número inteiro cujo quadrado é menor
ou igual ao número dado. Informalmente, pode - se dizer que isqrt()
retorna a parte inteira da raiz quadrada de um número passado para ela
como argumento.

from math import isqrt, sqrt

print(f"{isqrt(9) = }")  # => isqrt(9) = 3
print(f"{sqrt(9) = }")  # => sqrt(9) = 3.0

print(15*'-')

print(f"{isqrt(17) = }")  # => isqrt(17) = 4
print(f"{sqrt(17) = }")  # => sqrt(17) = 4.123105625617661

print(15*'-')

# -------------------------------------------------------------

# math.dist() => Retorna o valor da distância euclidiana entre
dois pontos passados como argumentos sejam eles pontos 2 ou 3D.

from math import dist

# Pontos 3D:
p3d1 = (12, 50, 40)
p3d2 = (6, 7, 13)

# Pontos 2D:
p2d1 = [12, 50]
p2d2 = [6, 7]

print(f"{dist(p3d1, p3d2) = }")  # => dist(p3d1, p3d2) = 51.12729212465687

print(15*'-')

print(f"{dist(p2d1, p2d2) = }")  # => dist(p3d1, p3d2) = 51.12729212465687

print(15*'-')


# -------------------------------------------------------------


* math.hypot => Retorna a hipotenusa (ou Norma Euclidiana) de um triângulo
retângulo dado os comprimentos dos catetos. De maneira mais geral, ele
calcula a distância Euclidiana da origem (0, 0) a um ponto (x, y) em um
espaço bidimensional. No caso de três dimensões, ele calcula a distância
Euclidiana da origem a um ponto (x, y, z).

from math import hypot

p3d1 = (12, 50, 40)
p2d1 = [12, 50]

print(f"{hypot(*p3d1) = }")  # => hypot(*p3d1) = 65.14598989960932
print(f"hypot(*p3d1) = {hypot(*p3d1):.2f}")  # => hypot(*p3d1) = 65.15

print(15*'-')

print(f"{hypot(*p2d1) = }")  # => hypot(*p2d1) = 51.419840528729765
print(f"hypot(*p2d1) = {hypot(*p2d1):.2f}")  # => hypot(*p2d1) = 51.42

print(15*'-')

# -------------------------------------------------------------

- Estatística:

* statistic.fmean() => Calcula a média aritmética de números reais.

from statistics import fmean

real_values = [1.45, 6.789, 3.45, 89.98765]
integer_values = [1, 6, 3, 89]

print(f"fmean(real_values)= {fmean(real_values):.2f}")
# => fmean(real_values)= 25.4225.42
print(15*'-')

print(f"fmean(integer_values)= {fmean(integer_values)}")
# => fmean(integer_values)= 24.75
print(15*'-')

* statistic.geometric_mean() => Calcula a média geométrica de números
reais.

from statistics import geometric_mean

real_values = [1.45, 6.789, 3.45, 89.98765]
integer_values = [1, 6, 3, 89]

print(f"geometric_mean(real_values) = {geometric_mean(real_values):.2f}")
# => geometric_mean(real_values)= 7.44
print(15*'-')

print(f"geometric_mean(integer_values) = {geometric_mean(integer_values):.2f}")
# => geometric_mean(integer_values) = 6.33
print(15*'-')




* statistic.multimode() => Retorna o valor mais frequente em uma
sequência.

from statistics import multimode

seq1 = "Geek University"
seq2 = [3, 5, 3, 8, 7, 9, 5, 3]
seq3 = [1, 2, 3, 1, 2, 3, 4, 5, 6]

print(f"{multimode(seq1) = }")  # => multimode(seq1) = ['e']
print(15*'-')
print(f"{multimode(seq2) = }")  # => multimode(seq2) = [3]
print(15*'-')
print(f"{multimode(seq3) = }")  # => multimode(seq3) = [1, 2, 3]
print(15*'-')


# -------------------------------------------------------------




"""


from statistics import multimode

seq1 = "Geek University"
seq2 = [3, 5, 3, 8, 7, 9, 5, 3]
seq3 = [1, 2, 3, 1, 2, 3, 4, 5, 6]

print(f"{multimode(seq1) = }")  # => multimode(seq1) = ['e']
print(15*'-')

print(f"{multimode(seq2) = }")  # => multimode(seq2) = [3]
print(15*'-')

print(f"{multimode(seq3) = }")  # => multimode(seq3) = [1, 2, 3]
print(15*'-')

