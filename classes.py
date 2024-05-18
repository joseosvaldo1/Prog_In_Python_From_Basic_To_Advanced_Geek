"""
POO - Classes:

- Em POO, classes nada mais são do modelos dos objetos
do mundo real sendo representados computacionalmente.

- Imagine que você queira fazer um sistema para automatizar
o controle das lâmpadas da sua casa.

- Classes podem conter:
	* Atributos => Representam as características do objeto,
	ou seja, pelos atributos conseguimos representar
	computacionalmente os estados de um objeto. No caso da
	lâmpada, possivelmente iríamos querer saber se a lâmpada
	é 110 ou 220, sua cor, sua luminosidade, etc.
	* Métodos (funções) => Representam os comportamentos do
	objeto, ou seja, as ações que este objeto pode realizar
	em seu sistema. No caso da lâmpada, por exemplo, um
	comportamento comum que muito provavelmente iríamos querer
	representar no nosso sistema é o de ligar e de desligar
	a mesma.


- Em Python, para definir uma classe utilizamos a palavra
reservada class.

- Em Python, utilizamos a palavra reservada pass quando temos
um bloco de código que ainda não está implementado.

- Quando nomeamos nossas classes em Python, utilizamos por
convenção o nome das mesmas com inicial maiúscula. Se o nome
for composto, utiliza-se as inicias de ambas as palavras
em maiúsculas todas juntas (padrão Camel Case).

- Dica Geek: Em computação, não utilizamos: acentuação, caracteres
especiais, espaços em branco ou similares para nomes de classes,
atributos, métodos, arquivos, diretórios, etc.


- Quando estamos planejando um software e definimos quais classes
teremos que ter no sistema, chamamos estes objetos que serão
mapeados para classes de entidades.


"""

class Lamp:
	pass


class CurrentAccount:
	pass


class Product:
	pass


class User:
	pass


class Int:
	pass


lamp = Lamp()

integer = Int()

print(f"type(lamp) = {type(lamp)}")  # => type(lamp) =
# <class '__main__.LightBulb'>

print(f"type(1) = {type(1)}")  # => type(1) = <class 'int'>
print(f"type(integer) = {type(integer)}")  # => type(integer) =
# <class '__main__.Int'>

# As classs internas do Python tem inicial minúscula para
# para diferenciar das classes criadas pelos desenvolvedores.
