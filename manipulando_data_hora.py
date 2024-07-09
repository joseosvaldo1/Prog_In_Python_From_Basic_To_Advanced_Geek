"""
Manipulando Data e Hora:

- Python tem um módulo built-in (integrado) para se trabalhar
com data e hora chamado datetime.
- O módulo datetime em Python fornece classes para manipulação de
datas e horas. Ele permite a criação de objetos que representam
instantes específicos no tempo, bem como a realização de operações
com esses objetos, como a adição ou subtração de períodos de tempo.

# -----------------------------------------------------------------

import datetime

# print("Métodos e Atributos do Módulo Datetime:")
# print(f"dir(datetime) = {dir(datetime)}")
# dir(datetime) = ['MAXYEAR', 'MINYEAR', 'UTC', '__all__',
# '__builtins__', '__cached__', '__doc__', '__file__',
# '__loader__', '__name__', '__package__', '__spec__',
# 'date', 'datetime', 'datetime_CAPI', 'time', 'timedelta',
# 'timezone', 'tzinfo']

# MAXYEAR:
print(datetime.MAXYEAR)  # => datetime.MAXYEAR => 9999
print(15*'-')

# MINYEAR:
print(datetime.MINYEAR)  # => datetime.MINYEAR => 1
print(15*'-')

# O método now() da classe datetime retorna a data
# e a hora correntes:

print(datetime.datetime.now())  # => 2024-07-09 16:42:15.279988
print(15*'-')

# Verificando a representação de datetime.datetime.now() -
# por meio do método repr() - repr(datetime.datetime.now()):
print(repr(datetime.datetime.now()))  # => datetime.datetime(2024, 7,
# 9, 16, 44, 9, 477148)
print(15*'-')

# datetime.datetime.now(year, month, day, hour, minute,
# second, microsecond)

# Podemos usar o método replace() para fazer ajustes na data/hora:
start = datetime.datetime.now()

print(f"BEFORE - start = {start}")

print(15*'-')

start = start.replace(hour=16, minute=0, second=0, microsecond=0)

print(f"AFTER - start = {start}")

print(15*'-')

# -----------------------------------------------------------------


event = datetime.datetime(2025, 1, 1, 0)

print(type(event))         # => <class 'datetime.datetime'>
print(type('31/12/2024'))  # => <class 'str'>

print(event)  # event => 2025-01-01 00:00:00

print(15*'-')

# Recebendo dados do usuário e convertendo para data:

day_of_birth = input('Enter your date of bith (dd/mm/yyyy): ')
day_of_birth = day_of_birth.split('/')
day_of_birth = datetime.datetime(int(day_of_birth[2]),
                                 int(day_of_birth[1]),
                                 int(day_of_birth[0]))

print(day_of_birth)
print(type(day_of_birth))

print(15*'-')


# -----------------------------------------------------------------



"""

import datetime


# Fazendo acesso individual dos elementos de data e hora:
event = datetime.datetime.now()

print(event.year)         # => event.year => 2024
print(event.month)        # => event.month => 7
print(event.day)          # => event.day => 9
print(event.hour)         # => event.hour => 17
print(event.minute)       # => event.minute => 12
print(event.second)       # => # => event.second => 12
print(event.microsecond)  # => event.microsecond => 480086

