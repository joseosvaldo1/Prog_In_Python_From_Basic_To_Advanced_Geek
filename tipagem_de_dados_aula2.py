"""
# Checagem de Tipos em Python:
# Aula 2 - Tipagem de Dados - Dinâmnica x Estática:

- A tipagem de dados dinâmica em Python significa que o tipo de uma
variável é determinado automaticamente pelo interpretador no momento
da atribuição do valor, em vez de ser especificado explicitamente
pelo programador. Isso permite uma maior flexibilidade na escrita do
código, mas também requer uma boa compreensão dos tipos de dados
para evitar erros.

- Aqui estão os principais pontos sobre a tipagem dinâmica em Python:

* Atribuição de Variáveis:
        Em Python, você pode atribuir qualquer valor a uma variável
    sem declarar seu tipo. O interpretador deduz o tipo a partir
    do valor atribuído.

	x = 10        # x é um inteiro
	x = "Hello"   # x agora é uma string
	x = 3.14      # x agora é um ponto flutuante

* Tipo de Variável em Tempo de Execução:
	O tipo da variável pode mudar durante a execução do programa,
	dependendo do valor atribuído.

	y = [1, 2, 3]  # y é uma lista
	y = {"a": 1}   # y agora é um dicionário

* Funções e Tipagem Dinâmica:
	As funções em Python também não exigem a declaração de tipos de
parâmetros ou de retorno. Isso significa que uma função pode aceitar
diferentes tipos de dados como argumentos.

	def add(a, b):
        return a + b

	print(add(2, 3))         # Saída: 5
	print(add("foo", "bar")) # Saída: "foobar"

* Verificação de Tipo:
	Para garantir que uma variável tenha um tipo específico antes
	de realizar uma operação, você pode usar a função isinstance.

	z = 42
	if isinstance(z, int):
        print("z é um inteiro")

- Tipagem Fraca vs. Tipagem Forte:
	Embora Python seja dinamicamente tipado, ele é considerado fortemente
tipado. Isso significa que operações entre tipos incompatíveis não são
permitidas sem conversão explícita.

print(10 + "20")  # Erro: TypeError: unsupported operand type(s)
				  # for +: 'int' and 'str'

- Anotações de Tipo (Type Hints):
	A partir do Python 3.5, foram introduzidas anotações de tipo
(type hints) que permitem aos programadores especificar os tipos
esperados para variáveis e funções. Essas anotações não afetam a
execução do código, mas podem ser úteis para ferramentas de análise
estática e para melhorar a legibilidade do código.

    def greet(name: str) -> str:
        return "Hello, " + name

    nome: str = "Alice"

- Benefícios da Tipagem Dinâmica

    * Flexibilidade: Permite que você escreva funções genéricas que
    podem operar em diferentes tipos de dados.
    * Rapidez na Prototipação: Facilita a escrita e modificação do
    código sem a necessidade de declarações explícitas de tipos.

- Desvantagens da Tipagem Dinâmica

    * Erros de Tipo em Tempo de Execução: Erros relacionados a tipos
    podem não ser detectados até que o código seja executado.
    * Legibilidade e Manutenibilidade: Em grandes projetos, pode ser
    mais difícil entender e manter o código devido à falta de
    informações explícitas sobre tipos.

- A tipagem dinâmica é uma das características que torna Python uma
linguagem poderosa e fácil de usar, especialmente para prototipação e
desenvolvimento rápido. No entanto, é importante usar boas práticas de
programação e, quando possível, utilizar anotações de tipo para aumentar
a robustez e a clareza do código.


# -----------------------------------------------------------------


idade = 42

print(f"type(idade): {type(idade)}")  # => type(idade): <class 'int'>

idade = "Forty-two"

print(f"type(idade): {type(idade)}")  # => type(idade): <class 'str'>


# -----------------------------------------------------------------


if True:
	result = 1 + 'Geek'  # =>
else:
	result = 1 + 41

print(result)  # => TypeError: unsupported operand type(s)
# for +: 'int' and 'str'

# -----------------------------------------------------------------




"""



