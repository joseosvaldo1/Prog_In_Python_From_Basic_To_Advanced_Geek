"""
# Assertions (Afirmações/Checagens/Questionamentos):

- Em Python, utilizamos a palavra reservada 'assert' para
realizar simples afirmações utilizadas nos testes.

- Utilizamos o 'assert' em uma expressão que queremos
checar se é válida ou não. Se a expressão for verdadeira,
o assert retornará None e, caso seja falsa, levantará um
erro do tipo AssertionError.


Observações:
1) Nós podemos especificar opcionalmente um segundo arumento
ou mensagem de erro personalizada para o assert.
2) A palavra assert pode ser utilizada em qualquer em função
ou código não sendo exclusivamente utilizada nos testes.


# ALERTA - Cuidado ao utilizar 'assert': Se uma aplicação
Python for executada com o parâmetro -O, nenhum assertion
será validado, ou seja, todas as suas validações já eram.

"""


def sum_positive_numbers(a, b):
	assert a > 0 and b > 0, 'Both numbers given must be postive'
	return a + b


ret_1 = sum_positive_numbers(2, 4)
print(f'ret_1: {ret_1}')  # => ret_1: 6
print(15*'-')

# ret_2 = sum_positive_numbers(-2, 4)
# print(f'ret_2: {ret_2}')  # => # => ret_2: AssertionError: Both
# numbers given must be postive
# print(15*'-')


def eat_fast_food(food_name):
	eat_food_list = ['pizza', 'icecream', 'candies',
	                 'French fries', 'hotdog']
	assert food_name in eat_food_list, ('The food needs to '
	                                    'be fast food')

	return f"I'm eating {food_name}."


food_name = input('Enter a food_name: ')
print(eat_fast_food(food_name))

