"""


"""

# Entrada de Dados:
# print("Qual o seu nome?: ")
name = input("Qual o seu nome?: ")

# print("Qual a sua idade?: ")
age = int(input("Qual sua idade? "))
# int(age) => Realizou-se um 'cast' (passou de string para int)
# Cast é a conversão de um tipo de dado em outro.
# Qualquer tipo de dados que entrar por meio do método
# 'input' será considerado do tipo String.

# Processamento:


# Saída de Dados:
# Exemplos de print antigo - versão Python 2:
# print("Seja bem vindo(a), %s" % name)
# print("%s tem %d anos." % (name, age))

# Exemplos de print moderno- versão Python 3:
# print("Seja bem vindo(a), {0}.".format(name))
# print("{0} tem {1} anos".format(name, age))

# Exemplos de print atual versão Python 3.7:
print(25*"-")
print(f"Seja bem vindo(a), {name}.")
print(f"{name} tem {age} anos.")
print(f"{name} nasceu por volta de {2023-age}.")
print(25*"-")


