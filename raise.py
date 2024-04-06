"""
# Levantando os próprios com 'raise':

- Em Python, raise é uma palavra-chave utilizada para levantar (ou lançar)
uma exceção explicitamente. Quando um erro ou condição excepcional ocorre
em um programa, é comum utilizar o raise para notificar o Python de que
uma exceção específica deve ser gerada.

- A sintaxe básica para raise é: raise Excecao("mensagem de erro")
- Aqui, Excecao é o tipo da exceção que está sendo levantada, e "mensagem
de erro" é uma mensagem opcional que fornece mais detalhes sobre a exceção.

- Por exemplo, para levantar uma exceção do tipo ValueError quando um
argumento inválido é passado para uma função, você pode fazer algo assim:

def dividir(a, b):
    if b == 0:
        raise ValueError("Divisor não pode ser zero")
    return a / b

# Exemplo de uso
try:
    resultado = dividir(10, 0)
except ValueError as e:
    print(e)  # Imprime a mensagem de erro associada à exceção

- Quando o divisor é zero, a função dividir levanta uma exceção ValueError
com a mensagem "Divisor não pode ser zero". Esta exceção é então capturada
pelo bloco try...except para tratamento adequado.


# -------------------------------------------------------------

- raise: Lança exceções.

- Observação: O 'raise' não é uma função. Ele é uma palavra reservada
da linguagem Python.

- Para simplificar, pense no 'raise' como sendo útil para que possamos
criar nossas próprias exceções e mensagens.

- A forma geral de utilização é: raise TipoDeErro('Mensagem de Erro').

# Exemplos reais:

a)

def colore (texto, cor):
	if type(texto) is not str:
		raise TypeError("The 'text' parameter must be of type string.")
	if type(cor) is not str:
		raise TypeError("The 'cor' parameter must be of type string.")
	print(f"The text '{texto}' will be printed in color '{cor}'.")


colore("Geek", "blue")
# Saída: => The text 'Geek' will be printed in color 'blue'.
print(15*'-')
# colore("Geek", 4)
# Saída: => TypeError: The 'cor' parameter must be of type string.
# print(15*'-')
# colore(True, 'blue')
# Saída: => TypeError: The 'text' parameter must be of type string.
# print(15*'-')

b)
print("Exemplo_2:")

def colore (texto, cor):
	cores = ('green', 'yellow', 'blue', 'white')
	if type(texto) is not str:
		raise TypeError("The 'text' parameter must be of type string.")
	if type(cor) is not str:
		raise TypeError("The 'cor' parameter must be of type string.")
	if cor not in cores:
		raise ValueError(f"The color parameter must be between {cores}. ")

	print(f"The text '{texto}' will be printed in color '{cor}'.")


colore("Geek", "green")
# Saída: => The text 'Geek' will be printed in color 'blue'.
print(15*'-')

colore("Geek", "black")
# Saída: => ValueError: The color parameter must be between
# ('green', 'yellow', 'blue', 'white').
print(15*'-')

# Observação: Assim com o 'return', o 'raise' finaliza a função,
# ou seja, nada após o 'raise' será executado.

"""


# Exemplos reais:

print("Exemplo_2:")

def colore (texto, cor):
	cores = ('green', 'yellow', 'blue', 'white')
	if type(texto) is not str:
		raise TypeError("The 'text' parameter must be of type string.")
	if type(cor) is not str:
		raise TypeError("The 'cor' parameter must be of type string.")
	if cor not in cores:
		raise ValueError(f"The color parameter must be between {cores}. ")
		print("Depois do 'raise'.")
	print(f"The text '{texto}' will be printed in color '{cor}'.")


colore("Geek", "green")
# Saída: => The text 'Geek' will be printed in color 'blue'.
print(15*'-')

colore("Geek", "black")
# Saída: => ValueError: The color parameter must be between
# ('green', 'yellow', 'blue', 'white').
print(15*'-')

