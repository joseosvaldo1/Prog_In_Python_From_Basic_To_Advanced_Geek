"""
# Estruturas Lógicas: and, or, not, is

- Operadores Unários: not
- Operadores Binários: and, or, is

- Regras de Funcionamento para os Operadores Lógicos:
# Para o 'and', ambos os elementos devem ser verdadeiros.
# Para o 'or', um dos elementos deve ser verdadeiros.
# Para o 'not', o valor do booleano é invertido, ou seja,
se for True, vira False e, se for False, vira True
# Para o 'is' é usado para a comparação de um elemento
com outro.
"""

# _*_ coding: utf-8 _*_

# active = True
# logged = False
#
# if active:
#     print("Active user on the system")

# active = True
# logged = True
#
#
# if active and logged:
#     print("Welcome, user!")
# else:
#     print(f"You need to actiate your account. "
#           f"Please check your e-mail.")

# active = True
# logged = False


# if active or logged:
#     print("Welcome, user!")
# else:
#     print(f"You need to activate your account. "
#           f"Please check your e-mail.")


# active = True
# logged = False
#
# if not active:
#     print(f"active = {active}")
#     print(f"You need to active your account. "
#           f"Please check your email.")
# else:
#     print(f"Welcome, user!")
#
# print("'not' operator: ")
# print(not True)
# print(not False)

# active = False
# logged = False
#
# if active is False:
#     print(f"Boolean value for 'active' = {active}")
#     print(f"You need to active your account. "
#           f"Please check your email.")
# else:
#     print(f"Welcome, user!")

active = True
logged = False

if active:
    print(f"Welcome, user!")
else:
    print(f"Boolean value for 'active' = {active}")
    print(f"You need to active your account. "
          f"Please check your email.")


# Is User Active?:
print(f"Active User - active is True?: {active is True}")

# Is User Logged?:
print(f"Logged User - logged is True?: {logged is True}")


name1 = "Geek"
name2 = "GEEK"
print(f"name1 = {name1}")
print(f"name isupper() = {name1.isupper()}")
print(f"name2 = {name2}")
print(f"name isupper() = {name2.isupper()}")