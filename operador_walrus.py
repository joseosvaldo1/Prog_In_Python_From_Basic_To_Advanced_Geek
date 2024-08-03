"""
# Novos Recursos do Python:
- Operador Walrus (do inglês, morsa):

- O operador walrus (:=), também conhecido como operador de atribuição,
foi incorporado ao Python na versão 3.8. Ele permite a atribuição de
valores a variáveis como parte de uma expressão, possibilitando uma
escrita de código mais concisa e potencialmente mais eficiente em
alguns casos.

- O operador walrus permite fazer a atribuição e o retorno
de um valor em uma única expressão.
- Sintaxe do operador walrus: variavel := expressao




"""

print("Without using the walrus operator - :=")

name = "Geek University"
print(name)

print(15*'-')

print("With using the walrus operator - :=")

print(name := 'Geek University')

print(15*'-')

# Sem o uso do operador Walrus:
# fruit_basket = []
# fruit = input("Enter a fruit name: ")
#
# while fruit != 'jaca':
# 	fruit_basket.append(fruit)
# 	fruit = input("Enter a fruit name: ")

# Utilizando o operador walrus:

fruit_basket = []

while (fruit := input("Enter a fruit: ")) != 'jaca':
	fruit_basket.append(fruit_basket)

