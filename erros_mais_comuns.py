"""
# Erros Mais Comuns Python:

- ATENçÂO: É importante prestar atenção e aprender a ler as saídas
de erro geradas pela execução.

* Os erros mais comuns:

1) SyntaxError: Ocorre quando o interpretador do Python encontra um
erro de sintaxe, ou seja, você escreveu algo que o interpretador do
Python não reconhece como parte da linguagem.

# Exemplos de SintaxError:

a)
# def function_wrong:  # => faltou os parênteses # => SyntaxError: expected '('
def function_wrong():
	print('Geek University')


function_wrong()

b)

# None = 1
# print(None)  # => SyntaxError: cannot assign to None

# def = 1
#
# print(def)  # => SyntaxError: invalid syntax

c)
# return  # => SyntaxError: 'return' outside function

# --------------------------------------------------------

2) NameError: Ocorre quando uma variável ou função não foi definida.

# Exemplos de NameError:

a)
# print(geek)  # => NameError: name 'geek' is not defined

b)
# geek()   # => NameError: name 'geek' is not defined

c)

a = 18

if a < 10:
	msg = 'É maior que 10'

print(msg)  # => NameError: name 'msg' is not defined

# A variável msg é de escopo local ao if, por isso o NameError.


# ----------------------------------------------------------

3) TypeError: Ocorre quando uma função/ação/operação é aplicada
a um tipo errado.

# Exemplos de TypeError:

a)
# print(len(5))  #  => TypeError: object of type 'int' has no len()

b)
# print('Geek' + 4)  # => TypeError: can only concatenate str (not "int")
# to str

# -------------------------------------------------------------

4) IndexError: Ocorre quando tentamos acessar um elemento em uma lista
ou outro tipo de dado indexado utilizando um índice inválido.

# Exemplos de IndexError:

a)
lista = ['Geek']
print(lista[0])  # => Geek
# print(lista[2])  # => IndexError: list index out of range

b)

lista = ['Geek']
print(lista[0])
print(lista[0][0])  # => G
# print(lista[0][10])  # => IndexError: string index out of range


c)

tupla = ('Geek')
print(tupla[0][0])     # => G
# print(tupla[0][10])  # => IndexError: string index out of range

# ------------------------------------------------------------

5) ValueError:

"""


# Exemplos de ValueError:





