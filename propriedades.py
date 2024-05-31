"""
# POO - Propriedades (Properties):

- A melhor forma de ter acesso a valores de atributos é
criando métodos para manipulá-los. Nós chamamos estes
métodos de acessores (getter methods) e métodos mutadores
(setter methods).

- Em linguagens de programação como Java, ao declararmos
atributos privados nas classes, costumamos criar métodos
públicos para manipulação desses atributos. Esses métodos
são conhecidos por getters e setters, onde os getter retornam
o valor dos atributos e os setters alteram o valor dos mesmos.

# --------------------------------------------------------------

class CurrentAccount:
    counter = 0
    def __init__(self, holder, balance, limit):
        self.__number = CurrentAccount.counter + 1
        self.__holder = holder
        self.__limit = limit
        self.__balance = balance
        CurrentAccount.counter += self.__number

    def statement(self):
        return (f"Balance of R$ {self.__balance:.2f} of the holder "
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

    # Métodos Acessores e Mutadores:
    # Getters and Setters Methods:
    def get_number(self):
        return self.__number

    def get_holder(self):
        return self.__holder

    def set_holder(self, holder):
        self.__holder = holder

    def get_balance(self):
        return self.__balance


    def get_limit(self):
        return self.__limit

    def set_limit(self, limit):
        self.__limit = limit



conta_1 = CurrentAccount("Felicity Jones", 3000, 5000)
conta_2 = CurrentAccount("Angelina Jolie", 2000, 4000)

print(15*'-')
print(f"conta_1.statement(): {conta_1.statement()}")
print(f"conta_2.statement(): {conta_2.statement()}")

print(15*'-')

# Somando-se a soma dos saltos:

# Usando Name Mangling (forma inadequada):

# sum_balance = (conta_1._CurrentAccount__balance +
#                 conta_2._CurrentAccount__balance)

# Usando Métodos Acessores (forma adequada):
sum_balance = conta_1.get_balance() + conta_2.get_balance()

print(f"The sum of balances is R$ {sum_balance:.2f}.")

print(15*'-')

print(f"conta_1.get_limit() BEFORE: R$ {conta_1.get_limit():.2f}")
print(f"conta_1.__dict__ BEFORE= {conta_1.__dict__}")
print(15*'-')
conta_1.set_limit(999999)
print(f"conta_1.get_limit() AFTER: R$ {conta_1.get_limit():.2f}")
print(f"conta_1.__dict__ AFTER = {conta_1.__dict__}")


# ----------------------------------------------------------------

"""


class CurrentAccount:
    counter = 0
    def __init__(self, holder, balance, limit):
        self.__number = CurrentAccount.counter + 1
        self.__holder = holder
        self.__limit = limit
        self.__balance = balance
        CurrentAccount.counter += self.__number

    # Métodos Acessores e Mutadores:
    # Getters and Setters Methods:
    @property
    def number(self):
      return self.__number

    @property
    def holder(self):
        return self.__holder

    @property
    def balance(self):
        return self.__balance

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, new_limit):
        self.__limit = new_limit

    # Some other public instance methods:
    def statement(self):
        return (f"Balance of R$ {self.__balance:.2f} of the holder "
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

    @property
    def total_value(self):
        return f"R$ {(self.__limit + self.__balance):.2f}"

conta_1 = CurrentAccount("Felicity Jones", 3000,
                         5000)
conta_2 = CurrentAccount("Angelina Jolie", 2000,
                         4000)

print(15*'-')
print(f"conta_1.statement(): {conta_1.statement()}")
print(f"conta_2.statement(): {conta_2.statement()}")

print(15*'-')

# Somando-se a soma dos saltos:

# Usando Name Mangling (forma inadequada):

# sum_balance = (conta_1._CurrentAccount__balance +
#                 conta_2._CurrentAccount__balance)

# Usando Métodos Acessores (forma adequada):
sum_balance = conta_1.balance + conta_2.balance

print(f"The sum of balances is R$ {sum_balance:.2f}.")

print(15*'-')

print(f"conta_1.get_limit() BEFORE: R$ {conta_1.limit:.2f}")
print(f"conta_1.__dict__ BEFORE= {conta_1.__dict__}")
print(15*'-')
conta_1.limit = 76543
print(f"conta_1.get_limit() AFTER: R$ {conta_1.limit:.2f}")
print(f"conta_1.__dict__ AFTER = {conta_1.__dict__}")
print(f"conta_1.limit = R$ {conta_1.limit:.2f}")
print(15*'-')
print("conta_1.total_value = " + conta_1.total_value)
print("conta_2.total_value = " + conta_2.total_value)
print(15*'-')