"""
# Len, Abs, Sum, Round:

* len(): Retornar o tamanho (ou seja, o número de itens) de im iterável.

# Só para revisar a função len():
print("Exemplos - função len():")

print(f"len('Geek University') = {len('Geek University')}")
print(15*'-')

print(f"len([1, 2, 3, 4, 5]) = {len([1, 2, 3, 4, 5])}")
print(15*'-')

print(f"len((1, 2, 3, 4, 5)) = {len((1, 2, 3, 4, 5))}")
print(15*'-')

print("len({1, 2, 3, 4, 5}) = " + str(len({1, 2, 3, 4, 5})))
print(15*'-')

print("len({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}) = "
	  + str(len({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})))
print(15*'-')

print(f"len(range(0,10) = {len(range(0,10))}")
print(15*'-')

# Pode debaixo dos panos, quando utilizamos a função len(),
# o interpretador faz o seguinte:

# __len()-__ => Dunder len
print(f"'Geek University'.__len__() = "
	  f"{'Geek University'.__len__()}")
print(15*'-')


# ------------------------------------------

abs(): Retorna o valor absoluto (sem sinal) de um número
inteiro ou real.

# Exemplos - função abs():

print(f"abs(-5) = {abs(-5)}")
print(15*'-')
print(f"abs(-5) = {abs(5)}")
print(15*'-')
print(f"abs(-3.14) = {abs(-3.14)}")
print(15*'-')
print(f"abs(3.14) = {abs(3.14)}")
print(15*'-')

# ------------------------------------------

sum(): Recebe como parâmetro um iterável que possui objetos
numéricos,podendo ter um valor inicial e retorna o somatório
total destes elementos incluindo o valor inicial.
Observação: O valor inicial default da função sum() é 0.

         def sum(*args, **kwargs): # real signature
         unknown
    '''
    Return the sum of a 'start' value (default: 0)
    plus an iterable of numbers

    When the iterable is empty, return the start value.
    This function is intended specifically for use
    with numeric values and may reject non-numeric
    types.

    Retorna a soma de um valor 'inicial' (padrão: 0)
    mais um iterável de números.

    Quando o iterável estiver vazio, retorne o valor
    inicial.
    Esta função destina-se especificamente ao uso
    com valores numéricos e pode rejeitar valores
    não numéricos.

    '''
    pass

 # ------------------------------------------

# Exemplos - função sum():

print(f"sum([1, 2, 3, 4]) = {sum([1, 2, 3, 4, 5])}")
print(15*'-')

print(f"sum([1, 2, 3, 4], 5) = {sum([1, 2, 3, 4, 5], 5)}")
print(15*'-')

print(f"sum([3.145, 5.678]) = {sum([3.145, 5.678])}")
print(15*'-')

print(f"sum((1, 2, 3, 4, 5)) = {sum((1, 2, 3, 4, 5))}")
print(15*'-')

print("sum({1, 2, 3, 4, 5}) = "
	  + str(sum({1, 2, 3, 4, 5})))
print(15*'-')

print("sum({'a': 1,'b': 2, 'c': 3, 'd': 4, 'e': 5}) = "
	  + str(sum({'a': 1,'b': 2, 'c': 3, 'd': 4, 'e': 5}.values())))
print(15*'-')

# -------------------------------------------------------------

* round(): Retorna um número arredondado para 'n' dígitos de precisão
após a casa decimal. Se a precisão não for informada, retorna o inteiro
mais próximo da entrada.

def round(*args, **kwargs): # real signature unknown
    '''
    Round a number to a given precision in decimal digits.

    The return value is an integer if n digits is omitted or None.
    Otherwise
    the return value has the same type as the number.  n digits may
    be negative.

    Arredonde um número para uma determinada precisão em dígitos decimais.

    O valor de retorno será um número inteiro se n dígitos forem
    omitidos ou Nenhum.
    De outra forma, o valor de retorno tem o mesmo tipo que o número.
    n dígitos podem ser negativo.

    '''
    pass

"""

# Exemplos - round():

print(f"round(10.2) = {round(10.2)}")  # => 10
print(15*'-')
print(f"round(10.2, 3) = {round(10.2, 3)}")  # => 10.2
print(15*'-')
print(f"round(10.5) = {round(10.5)}")  # => 10
print(15*'-')
print(f"round(10.6) = {round(10.6)}")  # => 11
print(15*'-')
print(f"round(1.2121212121, 2) = {round(1.2121212121, 2)}")  # => 1.21
print(15*'-')
print(f"round(1.21999999, 2) = {round(1.21999999, 2)}")  # => 1.22
print(15*'-')

# Observação: Até X.5 sendo x um número inteiro, a função round
# arredonda para o inteiro X (arredonda para baixo). Acima de X.5
# (x.6, x.7, x.8, x.9), ele arredonda para o inteiro X+1.
# (arredonda para cima).

