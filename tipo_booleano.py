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
separador('_', 25)

print("Exemplo_2: ")
print("Operações Básicas: ")
# Negação (not):
# Fazendo a negação, se o valor da expressão
# a ser negada for verdadeiro, o resultado
# será falso. Caso contrário, será verdadeiro.
print(f"user1_ativo = {user1_ativo}")
print(f"not user1_ativo = {not user1_ativo}")
print(f"user2_ativo = {user2_ativo}")
print(f"not user2_ativo = {not user2_ativo}")
separador('_', 25)
