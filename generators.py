"""
# Generators (ou Generator Expressions):

- Em aulas anteriores, nós estudamos:
* List Comprehension;
* Dictionary Comprehension;
* Set Comprehension;

- No entanto, não vimos:
* Tuple Comprehension, pois elas se chamam 'Generators'

- No exemplo de uso do any(), vimos o seguinte:

names = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(f"names = {names}")
print(f"any([name[0] == 'C' for name in names]) = "
      f"{any([name[0] == 'C' for name in names])}")

print(15*'-')

- Poderíamos ter feito este exemplo usando generators:

print(f"any(name[0] == 'C' for name in names) = "
	  f"{any(name[0] == 'C' for name in names)}")

print(15*'-')

# List Comprehension:
result_lc = [name[0] == 'C' for name in names]
print(f"result_lc = {result_lc}")
print(f"type(result_lc) = {type(result_lc)}")
print(15*'-')

# Generator:
result_generator = (name[0] == 'C' for name in names)
print(f"result_generator = {result_generator}")
print(f"type(result_generator) = {type(result_generator)}")
print(15*'-')

# Observação: O generator é mais performático que o list
# comprehension ocupando menos recurso em memória.

# -------------------------------------------------------

from sys import getsizeof

# 'getsizeof()' => Retorna a quantidade de bytes em memória
# do elemento passado como parâmetro.

print(f"getsizeof('Geek') = {getsizeof('Geek')}")
print(15*'-')
print(f"getsizeof('University') = {getsizeof('University')}")
print(15*'-')
print(f"getsizeof(9) = {getsizeof(9)}")
print(15*'-')
print(f"getsizeof(91) = {getsizeof(91)}")
print(15*'-')
print(f"getsizeof(92345668823) = {getsizeof(92345668823)}")
print(15*'-')
print(f"getsizeof(True) = {getsizeof(True)}")
print(15*'-')


# Observação: Em se tratando de String, quanto maior a string,
# maior o espaço que ela ocupará.

# -----------------------------------------------

# Gerando uma lista de número com List Comprehension:

print("Para fazer a mesma coisa, gastamos em memória: ")

list_comp_size = getsizeof([x*10 for x in range(1000)])
print(f"list_comp_size = {list_comp_size}")
print(15*'-')

# Gerando uma lista de número com Set Comprehension:

set_comp_size = getsizeof({x*10 for x in range(1000)})
print(f"set_comp_size = {set_comp_size}")
print(15*'-')

# Gerando uma lista de número com Dictionary Comprehension:

dict_comp_size = getsizeof({x: x*10 for x in range(1000)})
print(f"dict_comp_size = {dict_comp_size}")
print(15*'-')

# Gerando uma lista de número com Generator:

generator_size = getsizeof((x*10 for x in range(1000)))
print(f"generator_size = {generator_size}")
print(15*'-')

print("Para fazer a mesma coisa, gastamos em memória: ")
print("Usando List Comprehension = " + str(list_comp_size) + " bytes")
print("Usando Set Comprehension = " + str(set_comp_size) + " bytes")
print("Usando Dictionary Comprehension = " + str(dict_comp_size) + " bytes")
print("Usando Generator Expression = " + str(generator_size) + " bytes")


"""

# Podemos iterar em um generator object:

gen = (x*10 for x in range(1000))
print(f"gen = (x*10 for x in range(1000)) = {(x*10 for x in range(1000))}")
print(f"type(gen) = {type(gen)}")
print(15*'-')

print("Fazendo a iteração usando um loop 'for': ")
for number in gen:
	print(number)


