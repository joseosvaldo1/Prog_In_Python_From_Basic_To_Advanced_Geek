"""
# Tipo String:

- Em Python, um dado é do tipo string sempre que:
* Estiver entre aspas simples. Exemplos: 'uma string',
'234', 'a', 'True', '42.3'.
* Estiver entre aspas duplas. Exemplos: "uma string",
"234", "a", "True", "42.3".
* Estiver entre aspas simples triplas. Exemplos:
'''uma string''', '''234''', '''a''', '''True''',
'''42.3'''.
* Estiver entre aspas duplas triplas. Exemplos:
"""
# """uma string""", """234""", """a""", """True""",
# """42.3""".

def separador(sinal, quantidade):

    print(sinal*quantidade)
    print(" ")

print("----------Tipo String----------")
print("Exemplo_1: ")
name = 'Geek University'
print(f"name: {name}")
print(f"type(name): {type(name)}")

separador("-", 25)

print("Exemplo_2: ")
name_2 = "Gina's Bar"

"""
Observação: Como foi usado uma aspa simples dentro
da string name_2, deve-se usar as aspas duplas 
externamente.
"""

print(f"name_2: {name_2}")
print(f"type(name_2): {type(name_2)}")

separador("-", 25)

print("Exemplo_3: ")
# name_3 = 'Angelina \nJolie'
# De forma equivalente a de cima:
name_3 = """Angelina 
        Jolie"""
print(f"name_3: {name_3}")
print(f"type(name_3): {type(name_3)}")

separador("-", 25)

print("Exemplo_4: ")
# name_4 = '"Angelina" Jolie'
name_4 = "\"Angelina\" Jolie"
print(f"name_4: {name_4}")
print(f"type(name_4): {type(name_4)}")

separador("-", 25)

print("Exemplo_5: ")
name_5 = "Geek University"
#Alguns métodos em strings:
print(f"name_5: {name_5}")
print(f"name_5.upper: {name_5.upper()}")
print(f"name_5.lower: {name_5.lower()}")
print(f"name_5.split(): {name_5.split()}")
""" 
Observação: O método 'split' separa os elementos 
de uma string em uma lista de strings. Internamente,
o Python pega uma string e a transforma em uma lista 
de strings com seus caracteres individuais.
name_5 = "Geek University" 
name_5 =['G', 'e', 'e', 'k',' ', 'U', 'n', 
         'i', 'v', 'e', 'r', 's', 'i', 't', 
         'y']
"""
# Slices de Strings:
print(f"name_5[0:4] = {name_5[0:4]}")
print(f"name_5.split()[0]: {name_5.split()[0]}")
print(f"name_5[5:15] = {name_5[5:15]}")
print(f"name_5.split()[1]: {name_5.split()[1]}")

# Invertendo os elementos de uma string:
print(f"name_5[::-1]: {name_5[::-1]}")

# Substituindo elementos de uma string - replace():
print(f"name_5.replace('G','P') = {name_5.replace('G','P')}")
print(f"name_5.replace('e','i') = {name_5.replace('e','i')}")
separador("-", 25)

text = "socorram me subino onibus em marrocos"
print(f"text       = {text}")
print(f"text[::-1] = {text[::-1]}")


