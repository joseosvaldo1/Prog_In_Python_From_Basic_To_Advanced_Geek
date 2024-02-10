"""
Loop 'for':

Loop -> Estrutura de reptição:
for -> Um dos tipos de estrutura de repetição em Python

# Estrutura do for no C e no Java:
for (int i = 0; i < limitador; i++){
    bloco de código;
}

# Estrutura do for no Python:

for item in interável:
    #Execução do loop for
    Obs: bloco de código após quatro espaços de identação


- De forma geral, utilizamos loop para iterar sobre
sequencias ou sobre valores iteráveis.

- Exemplos de Iteráveis:
1) Strings;
    name = "Geek University"
2) Listas (list):
    lista = [1, 3, 5, 7, 9]
3) Range:
 numbers = range(1, 10)

Observação sobre o objeto range:

# range(valor_inicial, valor_final, step):
- Valor inicial -> É incluído na iteração;
- Valor final -> Não é incluído na iteração;
- Step (ou passo) -> É o incremento da iteração,
sendo igual a 1 por padrão.
numbers = range(1,6)
print(numbers)
1
2
3
4
5
6 => Não é incluído

numbers2 = range(1,7,2)
print(numbers2)
1
3
5
7 => não é incluído

Observações sobre a classe enumerate:
Help on class enumerate in module builtins:

class enumerate(object)
   enumerate(iterable, start=0)

   Return an enumerate object.

     iterable
       an object supporting iteration

   The enumerate object yields pairs containing a
   count (from start, which
   defaults to zero) and a value yielded by the
   iterable argument.

   enumerate is useful for obtaining an indexed list:
        (0, seq[0]), (1, seq[1]), (2, seq[2]), ...

Methods defined here:

   __getattribute__(self, name, /)
       Return getattr(self, name).

   __iter__(self, /)
       Implement iter(self).

   __next__(self, /)
       Implement next(self).

   __reduce__(...)
      Return state information for pickling.

  -------------------------------------------
   Class methods defined here:

   __class_getitem__(...) from builtins.type
       See PEP 585
Static methods defined here:

   __new__(*args, **kwargs) from builtins.type
      Create and return a new object.  See help(type)
        for accurate signature.

Observação sobre o uso da 'enumerate':
- O 'underline' pode ser utilizado no lugar do
índice ou do valor quando queremos descartá-lo.

for index, value enumerate(iterable):
    print(index + " - " + value)

for _, value enumerate(iterable):
    print(value)

for index,_ enumerate(iterable):
    print(index)

Observação sobre a função 'print':
print(*args, sep=' ', end='\n', file=None, flush=False)
    Prints the values to a stream, or to sys.stdout by
    default.

    sep
      string inserted between values, default a space.
    end
      string appended after the last value, default a
      newline.
    file
      a file-like object (stream); defaults to the
      current sys.stdout.
    flush
      whether to forcibly flush the stream.



"""

print("Loop For: ")
print("Exemplos de iteráveis: ")

name = "Geek University"
lista = [1, 3, 5, 7, 9]
numbers = range(1,10)

# Exemplo_1 - Iterando sobre uma string:
print("Iterando sobre a string 'name': ")
print(f"name = {name}")
for letra in name:
    print(letra)

print( )

# Exemplo_2 - Iterando sobre uma lista:
print("Iterando sobre 'lista': ")
print(f"lista = {lista}")
for number in lista:
    print(number)

print(" ")

# Exemplo_3 - Iterando sobre uma range:
print("Iterando sobre o range numbers: ")
print(f"numbers = {numbers}")
for number in numbers:
    print(number)

print(" ")

# Determinando os índices e valores na string name
# usando 'enumerate':

# Usando índice e letra na enumerate:
for index, letter in enumerate(name):
    print(f"name[{index}]: {letter}")

print (" ")
# Usando apenas a letra na enumerate:
for _, letter in enumerate(name):
    print(letter)
print(" ")

print("Trazendo valor-letra e índice: ")
for value in enumerate(name):
    print(value)
print(" ")
print("Trazendo apenas os índices: ")
for value in enumerate(name):
    print(value[0])
print(" ")
print("Trazendo apenas os valores - letras: ")
for value in enumerate(name):
    print(value[1])
print(" ")

# qtd = int(input("How many times should this loop run? "))
#
# for n in range(1,qtd):
#     print(f"Imprimindo {n}" )
# print(" ")

# qtd = int(input("How many times should this loop run? "))
#
# for n in range(1,qtd + 1):
#     print(f"Imprimindo {n}" )
# print(" ")

# qtd = int(input("How many times should this loop run? "))
# sum = 0
#
# for n in range(1, qtd + 1):
#     num = int(input(f"Informe o {n} / {qtd} valor: "))
#     sum = sum + num
#
# print(f"The sum is: {sum}")

# name = "Geek University"
# for letter in name:
#     print(letter, end=' ')

# Original: 'u+1F60D'
# Modificado: '\U0001F60D'

# emoji = '\U0001F60D'
# for _ in range(3):
#     for num in range(1, 11):
#         print(emoji*num)

# Original: 'u+1F60D'
# Modificado: '\U0001F60D'

emoji = '\U0001F605'
for _ in range(3):
     for num in range(1, 11):
         print(emoji*num)


