"""
Tipo Booleano:

- Originário da álgebra booleana (criada por George Boole).
- 2 Constantes: Verdaeiro (True) ou Falso (False).

True -> Verdadeiro
False -> Falso

Observação: Os valores booleanos devem ser sempre grafados
com a inicial maiúscula: True ou False.

Errado: true    Certo: True
Errado: false   Certo: False

#


"""
def separador(sinal, quantidade):

    print(sinal*quantidade)
    print(" ")

print("Exemplo_1: ")

print("Usuário Ativo: ")
user1_ativo = True
print(f"user1_ativo = {user1_ativo}")

user2_ativo = False
print(f"user2_ativo = {user2_ativo}")

user3_ativo = False
print(f"user3_ativo = {user3_ativo}")

user4_ativo = True
print(f"user4_ativo = {user4_ativo}")

logado = False
print(f"logado = {logado}")

separador('_', 25)

print("Exemplo_2: ")
print("Operações Básicas: ")
"""
# Negação (not):
# Fazendo a negação, se o valor da expressão
# a ser negada for verdadeiro, o resultado
# será falso. Caso contrário, será verdadeiro.
"""
print(f"user1_ativo = {user1_ativo}")
print(f"not user1_ativo = {not user1_ativo}")
print(f"user2_ativo = {user2_ativo}")
print(f"not user2_ativo = {not user2_ativo}")
separador('_', 25)


"""
# Or (ou):
- É uma operação binária, ou seja, depende sempre
de dois valores booleanos.
- Para que uma expressão de dois elementos unidos 
por um 'or' seja verdadeira, um ou outro deve ser
necessariamente verdadeiro.

- Tabela-Verdade para o 'or':
True or True  => True
True or False => True
False or True => True
False or False => False

"""
separador('_', 25)
print(f"user1_ativo or user2_ativo = "
      f"{user1_ativo or user2_ativo}")
print(f"user2_ativo or user3_ativo = "
      f"{user2_ativo or user3_ativo}")
print(f"user1_ativo or logado= "
      f"{user1_ativo or logado}")
print(f"user2_ativo or logado= "
      f"{user2_ativo or logado}")
separador('_', 25)
"""
# And (ou):
- Também é uma operação binária, ou seja, depende 
sempre de dois valores booleanos.
- Para que uma expressão de dois elementos unidos 
por um 'and' seja verdadeira, os dois elementos
devem obrigatoriamente ser verdadeiros;

- Tabela-Verdade para o 'and':
True and True  => True
True and False => False
False and True => False
False and False => False

"""
separador('_', 25)
print(f"user1_ativo and user4_ativo = "
      f"{user1_ativo and user4_ativo}")
print(f"user1_ativo and user2_ativo = "
      f"{user1_ativo and user2_ativo}")
print(f"user1_ativo and logado = "
      f"{user1_ativo and logado}")
print(f"user2_ativo and logado = "
      f"{user2_ativo and logado}")
separador('_', 25)
