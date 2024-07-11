"""
# Métodos de Data e Hora:

import datetime

now = datetime.datetime.now()

print(f"now = {now}")  # => now = 2024-07-09 20:51:09.550337
print(f"type(now) = {type(now)}")  # => type(now) =
# <class 'datetime.datetime'>
print(f"repr(now) = {repr(now)}")  # => repr(now) =
# datetime.datetime(2024, 7, 9, 20, 51, 9, 550337)

# Com o método now() podemos especificar um
# parâmetro nomeado timezone (tz) (fuso
# horário):

print(15*'-')

today = datetime.datetime.today()
print(f"today = {today}")
print(f"type(today) = {type(today)}")
print(f"repr(today) = {repr(today)}")

print(15*'-')

# Observações: A principal diferença entre now() e today() é que
# now() pode aceitar um argumento de fuso horário (tz), enquanto
# today() não aceita e sempre retorna a data e a hora locais.
# Ambos métodos retornam um objeto datetime com a data e a hora
# atuais.

# -----------------------------------------------------------------

# Método combine():

- O método combine() do módulo datetime em Python é utilizado para
criar um objeto datetime a partir de um objeto date e um objeto
time. Ele permite combinar uma data específica com um horário
específico para formar uma data e hora completas.


# -----------------------------------------------------------------

# # Mudanças ocorrendo meia-noite:

# system_maintenance = datetime.datetime.combine((datetime.datetime.now() +
#                                                datetime.timedelta(days=1)),
#                                                datetime.time())
#
# print(f"system_maintenance = {system_maintenance}")
# # => system_maintenance = 2024-07-10 00:00:00
# print(f"type(system_maintenance) = {type(system_maintenance)}")
# # => type(system_maintenance) = <class 'datetime.datetime'>
# print(f"repr(system_maintenance) = {type(system_maintenance)}")
# # => repr(system_maintenance) = <class 'datetime.datetime'>


# De forma mais legível:
from datetime import datetime, timedelta, time

# Obtendo a data e hora atuais:
now = datetime.now()

# Calculando a data de amanhã
tomorrow = now + timedelta(days=1)

# Definindo o horário como meia-noite:
midnight = time()

# Combinando a data de amanhã com a meia-noite para a manutenção
# do sistema:
system_maintenance = datetime.combine(tomorrow.date(), midnight)

print(f"system_maintenance = {system_maintenance}")
# => system_maintenance = 2024-07-10 00:00:00
print(f"type(system_maintenance) = {type(system_maintenance)}")
# => type(system_maintenance) = <class 'datetime.datetime'>
print(f"repr(system_maintenance) = {repr(system_maintenance)}")
# => repr(system_maintenance) = datetime.datetime(2024, 7, 10, 0, 0)

print(15*'-')

# -----------------------------------------------------------------


from datetime import datetime, time, timedelta

# Encontrando o dia da semana de um evento - weekday():

# Os dias da semana do método 'weekday()' começam em 0
# sendo 0 a designação de segunda-feira:

# weekday() - code --------- Day Of The Week
#      0                     Segunda-feira (Monday)
#      1                     Terça-feira (Tuesday)
#      2                     Quarta-feira (Wednesday)
#      3                     Quinta-feira (Thursday)
#      4                     Sexta-feira (Friday)
#      5                     Sábado (Saturday)
#      6                     Sunday (Domingo)

# Obtendo a data e hora atuais:
now = datetime.now()

# Calculando a data de amanhã
tomorrow = now + timedelta(days=1)

# Definindo o horário como meia-noite:
midnight = time()

# Combinando a data de amanhã com a meia-noite para a manutenção
# do sistema:
system_maintenance = datetime.combine(tomorrow.date(), midnight)

print(f"system_maintenance.weekday() = {system_maintenance.weekday()}")
# => system_maintenance.weekday() = 2 => quarta-feira


# -----------------------------------------------------------------


day_of_birth = input('Enter your date of birth (dd/mm/yyyy): ')
day_of_birth = day_of_birth.split('/')
day_of_birth = datetime(year=int(day_of_birth[2]),
                        month=int(day_of_birth[1]),
                        day=int(day_of_birth[0]))

print(day_of_birth)
print(type(day_of_birth))

if day_of_birth.weekday() == 0:
    print('You were born on Monday!')
elif day_of_birth.weekday() == 1:
    print('You were born on Tuesday!')
elif day_of_birth.weekday() == 2:
    print('You were born on Wednesday!')
elif day_of_birth.weekday() == 3:
    print('You were born on Thursday!')
elif day_of_birth.weekday() == 4:
    print('You were born on Friday!')
elif day_of_birth.weekday() == 5:
    print('You were born on Saturday!')
else:
    print('You were born on Sunday!')

print(15*'-')



# -----------------------------------------------------------------


# Formatando datas/horas com o método
# strftime() (String Format Time):

today = datetime.today()

print(f"today = {today}")  # => today = 2024-07-10
# 20:02:46.726722

print(15*'-')

today_formated_1 = today.strftime('%d/%m/%Y')
today_formated_2 = today.strftime('%d/%B/%y')
today_formated_3 = today.strftime('%d/%b/%Y')

print(f"today_formated_1 = {today_formated_1}")  # =>
# today_formated_1 = 10/07/2024
print(f"today_formated_2 = {today_formated_2}")  # =>
# today_formated_2 = 10/July/24
print(f"today_formated_3 = {today_formated_3}")  # =>
# today_formated_3 = 10/Jul/2024

print(15*'-')

# -----------------------------------------------------------------

from datetime import datetime


def format_date(date):
    if date.month == 1:
        return f"{date.day} de janeiro de {date.year}."
    elif date.month == 2:
        return f"{date.day} de fevereiro de {date.year}."
    elif date.month == 3:
        return f"{date.day} de março de {date.year}."
    elif date.month == 4:
        return f"{date.day} de abril de {date.year}."
    elif date.month == 5:
        return f"{date.day} de maio de {date.year}."
    elif date.month == 6:
        return f"{date.day} de junho de {date.year}."
    elif date.month == 7:
        return f"{date.day} de julho de {date.year}."
    elif date.month == 8:
        return f"{date.day} de agosto de {date.year}."
    elif date.month == 9:
        return f"{date.day} de setembro de {date.year}."
    elif date.month == 10:
        return f"{date.day} de outubro de {date.year}."
    elif date.month == 11:
        return f"{date.day} de novembro de {date.year}."
    else:
        return f"{date.day} de dezembro de {date.year}."


today = datetime.today()
print(f"today = {format_date(today)}")

print(15*'-')


# -----------------------------------------------------------------


from datetime import datetime
from textblob import TextBlob


def format_date(date):
    month_english = date.strftime('%B')
    month_blob = TextBlob(month_english)
    month_portuguese = month_blob.translate(to='pt-br')
    return f"{date.day} de {month_portuguese} de {date.year}."


today = datetime.today()
print(f"today = {format_date(today)}")

print(15*'-')

# Observação: O módulo TextBlob teve o método translate()
# descontinuado. Dessa forma, o código acima não funciona.

# -----------------------------------------------------------------


from datetime import datetime

# Transformando uma string em um objeto do tipo datetime:

birth_day = datetime.strptime('10/04/1988',
                              '%d/%m/%Y')
print(f"birth_day = {birth_day} ")
print(f"type(birth_day = 10/04/1988) = {type(birth_day)}")

print(15*'-')

birth_day_input = input("Enter your date of birth in "
                        "dd/mm/yyyy format: ")
birth_day = datetime.strptime(birth_day_input,
                              '%d/%m/%Y')

print(f"birth_day = {birth_day}")
print(f"type(birth_day) = {type(birth_day)}")

print(15*'-')



# -----------------------------------------------------------------


import datetime

# Trabalhando apenas com horas:

lunch_time = datetime.time(12, 30, 00)

print(f"lunch_time = {lunch_time}")  # => lunch_time = 12:30:00

print(15*'-')

# -----------------------------------------------------------------

import timeit

# Marcando o tempo de execução do nosso código
# com o método timeit():

# Loop for:

time_1 = timeit.timeit('"-".join(str(n) for n in range(100))',
                        number=10000)

print(f"time_1 = {time_1}")

print(15*'-')


# List Comprehension:

time_2 = timeit.timeit('"-".join([str(n) for n in range(100)])',
                        number=10000)

print(f"time_2 = {time_2}")

print(15*'-')

# Map:

time_3 = timeit.timeit('"-".join(map(str, range(100)))',
                        number=10000)

print(f"time_3 = {time_3}")

print(15*'-')


# -----------------------------------------------------------------

"""

import timeit, functools

def test(n):
    sum = 0
    for number in range(n*200):
        sum = sum + number**number + 4
    return sum


# print(f"test(5) = {test(5)}")

print(timeit.timeit(functools.partial(test, 2), number=10000))
# Tempo de execução: 31.62954786800401