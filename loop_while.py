"""
# Loop While:

- Em Python, o loop while é utilizado para repetir um
bloco de código enquanto uma condição especificada
for verdadeira. A estrutura básica do loop while é a
seguinte:

while condição:
    # código a ser repetido enquanto a condição for
    verdadeira

- A condição é uma expressão booleana que é avaliada antes
da execução do bloco de código. Se a condição for verdadeira,
o bloco de código é executado. Após a execução do bloco, a
condição é novamente verificada. Se ainda for verdadeira, o
bloco é executado novamente, e assim por diante. O loop
continua até que a condição seja avaliada como falsa.

Aqui está um exemplo simples de um loop while que conta
de 1 a 5:

contador = 1

while contador <= 5:
    print(contador)
    contador += 1

- Neste exemplo, o código dentro do loop será executado enquanto
a variável contador for menor ou igual a 5. A cada iteração, o
valor de contador é impresso e incrementado em 1. O loop
continua até que contador seja maior que 5.

- É importante ter cuidado ao usar loops while para evitar loops
infinitos. Certifique-se de que a condição eventualmente se
torne falsa, ou inclua uma instrução de controle (como break
ou return) para interromper o loop quando necessário.


# Forma Geral do While:
while (condição booleana de parada):
    bloco de comandos a ser executado se a condição for True

- O bloco do while será repetida enquanto a condição booleana
de parada for verdadeira. Quando ela se tornar falsa, o loop
será finalizado.

- Expressão booleana é toda expressão que só admite como
resultados possíveis 'verdadeiro - True' ou 'Falso - False'.
Exemplo de expressões booleanas: num = 5, num < 5.

# Exemplo_1:
number = 1

while number < 10:
    print(number)
    number += 1

# Observação: Em um loop while, é importante que cuidemos
# da condição de parada para impedir loop infinitos.

"""

# Exemplo_2:

response = " "

while response != 'sim':
    response = input("Já acabou, Jéssica? ")



