"""
-Entendendo e Explorando Ranges:

# Precisamos conhecer o loop 'for' para usar o objeto range;
# Precisamos conhecer o objeto range para trabalhar melhor
com o loop 'for'.

# Ranges são utilizados para gerar sequências numéricas de
forma não aleatória, mas de maneira especificada.

# Em Python, range é um tipo de objeto que representa uma
sequência imutável de números. É comumente utilizado em
loops para iterar sobre uma sequência de valores numéricos.
A função range pode ser chamada com até três argumentos:
start, stop e step.

A sintaxe básica da função range é a seguinte:

range(stop)
range(start, stop)
range(start, stop, step)

start: O valor inicial da sequência (opcional). Se não
especificado, é assumido como 0.
stop: O valor de parada da sequência (obrigatório).
Representa o primeiro valor que não está na sequência.
step: O intervalo entre os valores da sequência (opcional).
Se não especificado, é assumido como 1.

É importante notar que o valor de stop não está incluído na
sequência resultante. Por exemplo, range(5) gera os números
de 0 a 4.

Aqui estão alguns exemplos de uso da função range:

# Exemplo 1: range com um único argumento
for i in range(5):
    print(i)
# Saída: 0, 1, 2, 3, 4

# Exemplo 2: range com dois argumentos
for i in range(2, 8):
    print(i)
# Saída: 2, 3, 4, 5, 6, 7

# Exemplo 3: range com três argumentos
for i in range(1, 10, 2):
    print(i)
# Saída: 1, 3, 5, 7, 9
Note que o valor step determina o intervalo entre os números
na sequência. No exemplo 3, o intervalo é 2, então apenas os
números ímpares são gerados.

Além disso, a função range cria um objeto de tipo range,
que é eficiente em termos de memória, pois não armazena
todos os valores da sequência, apenas os parâmetros
iniciais e finais. Se necessário, você pode converter um
objeto de tipo range para uma lista usando a função list().

"""

print("---Entendendo e Explorando Ranges---")
print(" ")
print("Exemplo_Forma_1:")
print("range(valor_de_parada)")
print("range(11)")
for number in range(11):
    print(number)

print(" ")

print("Exemplo_Forma_2:")
print("range(valor_de_inicio, valor_de_parada)")
print("range(4,11)")
for number in range(4, 11):
    print(number)

print(" ")

print("Exemplo_Forma_3:")
print("range(valor_de_inicio, valor_de_parada, passo)")
print("range(5,55,5)")

for number in range(5, 55, 5):
    print(number)

print(" ")
# Observação: Valor de parada não incluído e valor inicial
# e passo especificados pelo usuário/desenvolvedor.

print("Exemplo_Forma_3:")
print("range(valor_inicial, valor_final, passo)")
print("range(10,-1,-1)")

for number in range(10, -1, -1):
    print(number)

print(" ")

# Observação: Valor de parada não incluído e valor inicial
# e passo especificados pelo usuário/desenvolvedor.

# Para transformar um objeto range em uma lista, usamos
# a função 'list':
range_object = range(10)
lista = list(range(10))
print(f"range_object: {range_object}")
print(f"lista = {lista}")