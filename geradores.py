"""
# Geradores:

- Geradores (generators) são iteradores (iterators).

Observação: Nem t o d o iterator é um generator.

- Generators pode ser criados com funções geradoras;
- Funções geradoras utilizam a palavra reservada 'yield';
- Generators podem ser criados com Expressões Geradoras;


- Diferenças entre Functions(Funções) e Generators Functions
(Funções Geradoras) - Quadro Comparativo:

-------------------------------------------------------------------
|    Funções (Functions)      |    Generators Functions            |
-------------------------------------------------------------------
|	Utilizam 'return'	      |    Utilizam 'yield'                |
-------------------------------------------------------------------
|  Retorna apenas um vez      |   Podem utilizar yied multiplas    |
                              |   vezes    						   |
-------------------------------------------------------------------
| Quando executada, retorna   |    Quando executada, retorna 	   |
| um valor                    |    um generator.                    |
|------------------------------------------------------------------|


# -----------------------------------------------------------------

# Exemplo de Função Geradora (Generator Function):
def count_until(maximum_value):
	counter = 1
	while counter <= maximum_value:
		yield counter
		counter += 1


# Observação: Uma Generator Function não é um Generator.
# Ela cria um generator (gerador).

gen = count_until(5)
print(f"type(gen) = {type(gen)}")
print(15*'-')
print("gen = count_auntil(5):")
print(f"next(gen) = {next(gen)}")  # => next(gen) = 1
print(f"next(gen) = {next(gen)}")  # => next(gen) = 2
print(f"next(gen) = {next(gen)}")  # => next(gen) = 3
print(f"next(gen) = {next(gen)}")  # => next(gen) = 4
print(f"next(gen) = {next(gen)}")  # => next(gen) = 5
# print(f"next(gen) = {next(gen)}") => StopIteration

print(15*'-')


# -----------------------------------------------------------------

gen_2 = count_until(10)

# Usando um loop for em gen_2:

print("gen_2 = count_until(10)")
for number in gen_2:
	print(number)


print(15*'-')


# -----------------------------------------------------------------

gen_3 = count_until(10)
print("count_until(10)")
print(f"next(gen_3) = {next(gen_3)}")  # => next(gen_3) = 1

print("Após chamar next(gen_3) = 1, fazendo um loop for teremos:")

for number in gen_3:
	print(number, end= " ")
# Saída - output: 2 3 4 5 6 7 8 9 10
print(" ")
print(15*'-')

"""


# Exemplo de Função Geradora (Generator Function):
def count_until(maximum_value):
	counter = 1
	while counter <= maximum_value:
		yield counter
		counter += 1


# Observação: Uma Generator Function não é um Generator.
# Ela cria um generator (gerador).

gen_3 = count_until(10)

# Transformando o gen_3 em uma lista:
print("gen_3 = count_until(10)")
print(f"list(gen_3) = {list(gen_3)}")



