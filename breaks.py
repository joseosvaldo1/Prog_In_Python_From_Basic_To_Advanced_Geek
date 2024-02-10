"""
# Saindo de Loops Com Break:

- Utilizamos 'break' para sair de loops de forma
forçada/projetada.


"""

#Exemplo_1:

for number in range(1, 11):
    if number == 6:
        break
    else:
        print(number)

print("I got out of the loop!")
print("Saí do loop!")

# Exemplo_2:

mesage = "Type 'end' to exit the program: "
while True:
    command = input(mesage)
    if command == 'end':
        break