"""
# POO - Abstração e Encapsulamento

- O grande objeto do programação orientada a objetos é
encapsular o nosso código dentro de um grupo lógico e
hierárquico utilizando classes.

Encapsular => cápsula => O ato de encapsular os elementos
de uma classe.

- Encapsulamento => Agrupamento de atributos e métodos.

            CLASSE
--------------------------------------
|		Atributos e Métodos           |
|_____________________________________|

# Relembrando Atributos e Métodos em Python:

- Imagine que temos uma classe chamada Person contendo um atributo
privado chamado __name e um método privado chamado __falar().

- Esses elementos privados só devem ou deveriam ser acessados
dentro da classe. Porém o Python não bloqueia esse acesso fora
da classe. Com Python acontece um fenômeno chamado Name
Mangling, que faz uma alteração na forma de se acessar os
elementos privados, conforme: _Classe__elemento.

Exemplo:
1) instancia._Person__name
2) instância._Person__falar()



Abstração em POO => É o ato de expor apenas dados relevantes de uma
classe, escondendo atributos e métodos privados de usuários.



"""


class CurrentAccount:
    counter = 400
    def __init__(self, holder, limit, balance):
        self.__number = CurrentAccount.counter + 1
        self.__holder = holder
        self.__limit = limit
        self.__balance = balance
        CurrentAccount.counter += self.__number

    def statement(self):
        print(f"Balance of R$ {self.__balance:.2f} of the holder "
			  f"{self.__holder} with limit R$ {self.__limit:.2f}. ")

    def deposit(self, value):
        if value > 0:
            if value > 0:
                self.__balance += value
            else:
                print("The value must be positive.")
        else:
            print("The value must be positive.")

    def withdraw(self, value):
        if self.__balance >= value:
            self.__balance -= value
        else:
            print("Insufficient bank balance.")

    def transfer(self, value, destiny_account):
        # Remover o valor do saldo da conta de origem
        self.__balance -= value
        self.__balance -= 10  # => taxa de transferência

        # Adicionar o valor na conta de destino:
        destiny_account.__balance += value


# Testando:
# conta_1 = CurrentAccount('Geek', 1500.00, 150.00)
#
# print(f"conta_1 = {conta_1}")  # => conta_1 =
#
# print(f"conta_1.__dict__ = {conta_1.__dict__}")  # => conta_1.__dict__ =
# # {'_CurrentAccount__number': 401, '_CurrentAccount__holder': 'Geek',
# # '_CurrentAccount__limit': 150.0, '_CurrentAccount__balance': 1500.0}
#
# conta_1.statement()  # => Balance of R$ 1500.00 of the holder
# Geek with limit R$ 150.00.

# print(f"conta_1._CurrentAccount__holder = "
# 	  f"{conta_1._CurrentAccount__holder}")  # => Name Mangling =>
# Acesso inadequado ao atributo privado da classe CurrentAccount

# conta_1._CurrentAccount__holder = "Angelina"
# print(15*'-')
# print(f"conta_1._CurrentAccount__holder = "
# 	  f"{conta_1._CurrentAccount__holder}")

# -----------------------------------------------------
# print(15*'-')
# print("Before making a deposit of R$ 150.00:")
# print(f"conta_1.__dict__ = {conta_1.__dict__}")
# conta_1.statement()
#
# conta_1.deposit(150.00)
#
# print(15*'-')
#
# print("After making a deposit of R$ 150.00:")
# print(f"conta_1.__dict__ = {conta_1.__dict__}")
# conta_1.statement()
#
# print(15*'-')
#
# print("After making a withdrw of R$ 200.00:")
# print(f"conta_1.__dict__ = {conta_1.__dict__}")
# conta_1.withdraw(200)
# conta_1.statement()
#
# print(15*'-')

# ------------------------------------------------------------

conta_1 = CurrentAccount('Angelina', 1500.00, 150.00)
conta_1.statement()

conta_2 = CurrentAccount('Felicity', 2000.00, 300)
conta_2.statement()

print(15*'-')
print("After bank transfer: ")
conta_1.transfer(100, conta_2)

conta_1.statement()
conta_2.statement()