"""
POO - Atributos:
- Atributos => Representam as características do objeto,
ou seja, pelos atributos conseguimos representar
computacionalmente os estados de um objeto.


- Em Python, dividimos os atributos em três grupos:
	* Atributos de Instância;
	* Atributos de Classe;
	* Atributos Dinâmicos.


# Atributos de Instância:

- São atributos declarados dentro do método construtor da classe.
Observação: Método construtor é um método especial utilizado para
a criação do objeto.
- Em Java, uma classe Lamp (Lâmpada), incluindo seus atributos,
ficaria mais ou menos assim:

public class Lamp(){
	private int voltage;
	public String color;
	protected boolean turnOn = False;

	public Lamp()
		this.voltage = voltage;
		this.color = color;
		this.turnON = turnOn;
}
	public int getVoltage(){
		return this.voltage;
	}

# -----------------------------------------------------------

- Atributos Públicos: Em Python, todos os membros de uma classe são
públicos por padrão. Qualquer atributo ou método que seja definido
em uma classe é público, o que significa que pode ser acessado tanto
dentro quanto fora da classe.

class MinhaClasse:
    def __init__(self):
        self.meu_atributo = "Eu sou público!"

- Atributos Protegidos(Protected): Atributos protegidos devem ser
acessados apenas dentro da classe e suas subclasses, não fora delas.
Em Python,não há uma maneira estrita de forçar isso, mas por convenção,
um atributo é considerado protegido se seu nome começar com um
sublinhado (_).


class MinhaClasse:
    def __init__(self):
        self._meu_atributo = "Eu sou protegido!"

- Atributos Privados (Private): Atributos privados devem ser acessados
apenas dentro da classe que os define. Em Python, se o nome de um
atributo começar com dois sublinhados (__), ele se torna privado.
Python muda o nome do atributo para evitar conflitos de nomes e
torná-lo menos acessível, mas tecnicamente ainda é possível acessá-lo
diretamente.


class MinhaClasse:
    def __init__(self):
        self.__meu_atributo = "Eu sou privado!"

- Lembre-se, estas são convenções e não são estritamente aplicadas
pelo Python. A ideia é que programadores respeitem essas convenções
ao escrever código.

"""

# Atributos Públicos e Atributos Privados:

# Classes de Instâncias com Atributos Públicos:
class Lamp:
	# Método Construtor em Python => __init__
	def __init__(self, voltage, color):
		self._voltage = voltage
		self._color = color
		self._turn_on = False


# Observações:
# 1) Em Python, devemos declarar os atributos de instância
# dentro do método construtor;
# 2) Em Python, os atributos privamos são determinados pela
# presença de dois underlines antes deles (__voltage, __color,
# __turn_on).
# 3) O 'self' indica o objeto que está executando o método e
# sempre será o primeiro parâmetros dos métodos em uma classe.
# 4) Em Python, por convenção, ficou estabelecido que t o d o
# atributo de uma classe é público, ou seja, pode ser acessado em
# t o d o o projeto. Caso queiramos demonstrar que determinado
# atributo deva ser tratado como privado, ou seja, que deva ser
# acessado / utilizado dentro da própria classe onde está declarado,
# utilizamos duplo underscore(__) no início de seu nome. Isto
# também é conhecimento como Name Mangling.

class CurrentAccount:
	def __init__(self, number, limit, balance):
		self.number = number
		self.limit = limit
		self.balance = balance


# class Product:
# 	def __init__(self, name, description, price):
# 		self.name = name
# 		self.description = description
# 		self.price = price


class User:
	def __init__(self, name, email, password):
		self.name = name
		self.email = email
		self.password = password


# Classes de Instâncias com Atributos Privados:

class Acces:
	def __init__(self, email, password):
		self.email = email
		self.__password = password

	def show_password(self):
		return self.__password

	def show_email(self):
		return self.email

# Observação: Lembre-se que isso é apenas uma convenção,ou seja,
# a linguagem Python não vai impedir que façamos acesso aos
# atributos sinalizados como privados fora da classe.

# Exemplo:


user = Acces('user@gmail.com', '123456')


print(f"user.email = {user.email}")
# print(f"user.password = {user.__password}")  # => AttributeError:
# 'Acces' object has no attribute '__password'
print(dir(user))
print(f"user._Acces__password = {user._Acces__password}")
# Temos acesso ao atributo password, mas não deveríamos.
# Name Mangling.

print(15*'-')
print(f"show_password() = {user.show_password()}")
print(f"show_email() = {user.show_email()}")


# O que signfica atributos de instâncias?
# Significa que, ao criarmos instâncias / objetos de uma classe,
# todas as instâncias terão estes atributos.

user1 = Acces('user1@gmail.com', '123456')
user2 = Acces('user2@gmail.com', '654321')

print(f"user1.show_email() = {user1.show_email()}")
print(f"user2.show_email() = {user2.show_email()}")


# Atributos de Classe:

# p1 = Product('Playstation 4', 'Video Game', 'R$ 2.300,00')
# p2 = Product('XBox', 'Video Game', 'R$ 4.500,00')

# Atributos de instância são aqueles das instâncias objetos criados.
# Nos exemplos acima, 'Playtation 4', 'Video Game' e 'R$ 2.500,00'
# são os atributos da instância p1, enquanto 'XBox', 'Video Game' e
# 'R$ 4.500,00' são atributos da instância p2.

# Atributos de Classe s]ao atributos que são declarados diretamente
# na classe, ou seja, fora do método construtor da classe.
# Geralmente, já inicializamos com um valor para tal atributo e
# este valor é compartilhado entre todas as instâncias da classe,
# ou seja, ao invés de cada instância da classe ter seus próprios
# valores como é o caso dos atributos de instância, com os atributos
# de classe, todas as instâncias terão o mesmo valor para este
# atributo.

# Vamos refatorar a classe Product para incluirmos
# atributos de classe nela:

class Product:
	# Atributo de Classe:
	tax = 1.05  # => Acréscimo de 0.05 (5%) de imposto.
	counter = 0

	def __init__(self, name, description, price):
		self.id = Product.counter + 1
		self.name = name
		self.description = description
		self.price = price*Product.tax
		Product.counter += self.id



print(15*'-')

p1 = Product('Playstation 4', 'Video Game', 2300)
p2 = Product('XBox', 'Video Game', 4500)

print(f"p1.tax = {p1.tax}")  # => Acesso possível, mas incorreto
print(f"p2.tax = {p2.tax}")  # => Acesso possível, mas incorreto

print(15*'-')

print(f"p1.price = R$ {p1.price:.2f}")
print(f"p2.price = R$ {p2.price:.2f}")

print(15*'-')

# Observação: Não precisamos criar uma instância para de uma
# classe para fazer acesso a um atributo de uma classe.
print(f"Product.tax = {Product.tax:.2f}")  # Acesso correto

print(15*'-')

print(f"p1.id = {p1.id}")
print(f"p2.id = {p2.id}")

print(15*'-')

# Observações:
# 1) Para fazer acesso ao atributo de classe, usa-se a seguinte
# terminologia: nome_da_classe.atributo_de_classe
# 2) Em linguagens como Java, os atributos conhecidos como
# atributos de classe são chamados de atributos de estáticos.


# Atributos Dinâmicos => Um atributo de instância de pode ser
# criado em tempo de execução.

# Observação: Um atributo dinâmico será exclusivo da instância
# que o criou.

p3 = Product('Rice', 'grocery_store', 5.99)

# Criando um atributo dinâmico em tempo de execução:

p3.weight = '5 Kg'  # => Note que classe Product não existe o
# atributo 'weight'.

print(f"Product.p3 = {p3.name}, {p3.description}, "
	  f"R$ {p3.price:.2f}, {p3.weight}")

# print(f"Product.p1 = {p1.name}, {p1.description}, "
# 	  f"R$ {p1.price:.2f}, {p1.weight}")

# Output - Saída: AttributeError: 'Product' object has no
# attribute 'weight'

print(15*'-')


# Deletando atributos:

# Verificando a estrutura dos objetos p1 e p3:

print(f"p1.__dict__ = {p1.__dict__}")  # => p1.__dict__ = {
# 'id': 1, 'name': 'Playstation 4', 'description':
# 'Video Game', 'price': 2415.0}

print(f"p3.__dict__ = {p3.__dict__}")  # => p3.__dict__ = {
# 'id': 4, 'name': 'Rice', 'description': 'grocery_store',
# 'price': 6.2895, 'weight': '5 Kg'}

# print(f"Product.__dict__ = {Product.__dict__}")  # => Product.__dict__ =
# {'__module__': '__main__', 'tax': 1.05, 'counter': 7,
# '__init__': <function Product.__init__ at 0x7368adbf3e20>,
# '__dict__': <attribute '__dict__' of 'Product' objects>,
# '__weakref__': <attribute '__weakref__' of 'Product' objects>,
# '__doc__': None}

print(15*'-')

del p3.weight   # => Removendo atributo dinâmico (weight de p3)
# del p3.price  # => Removendo atributo estático (price de p3)

print(f"p1.__dict__ = {p1.__dict__}")  # => p1.__dict__ = {
# 'id': 1, 'name': 'Playstation 4', 'description': 'Video Game',
# 'price': 2415.0}
print(f"p3.__dict__ = {p3.__dict__}")  # => p3.__dict__ = {
# 'id': 4, 'name': 'Rice', 'description': 'grocery_store',
# 'price': 6.2895}

