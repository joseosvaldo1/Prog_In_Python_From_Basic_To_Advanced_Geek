"""
# Escopo de Variáveis:
- Dois tipos de escopo:
1) Variáveis Globais:
- Variáveis globais são reconhecidas em todo o programa,
ou seja, seu escopo comprende o programa inteiro.

2) Variáveis Locais
- Variáveis locais são reconhecidas apenas no bloco
onde foram declaradas, ou seja, seu escopo está limitado
ao bloco onde foi declarada.

# Para declarar variáveis em Python, fazemos:
name_da_variavel = valor_da_variavel

Observação: Python é uma linguagem de tipagem dinâmica,
ou seja, ao declararmos uma variável não indicamos o tipo
de dado da mesma. Este tipo é inferido ao atribuirmos
um dado valor a variável

"""
def separador(sinal, quantidade):

    print(sinal*quantidade)
    print(" ")


print("---Escopo de Variáveis em Python---")
print("Exemplo_1: ")

number = 42 # => Variável Global
print(f"number = {number}")
print(f"type(number) = {type(number)}")
print("-----------------")
# Realizando a reatribuição:
print("Realizando a reatribuição de 'number':")
number = 'Geek'
print(f"number = {number}")
print(f"type(number) = {type(number)}")

separador("_", 25)

print("Exemplo_2: ")
numero = 2
novo = 0

if numero > 10:
    novo = numero + 10
    print(novo)
"""
Observação: A variável 'novo' está declarada localmente
em relação ao bloco do 'if'. Por tanto, ela é local.
Se não tívemos declarado a variável 'novo' fora do 'if'
e numero > 10 for falsa, o código não entrará dentro do 
bloco do 'if' e a variável 'novo' não seria criada.
"""
print(novo)


