"""
# Trabalhando com deltas de data e hora:

import datetime

# Data atual:
current_date = datetime.datetime.now()

# Data para ocorrer um evento futuro:
birthday = datetime.datetime(2024,10,5,17)

# Calculando o delta (diferença de tempo):
time_for_event = birthday - current_date

print(type(time_for_event))  # => <class 'datetime.timedelta'>

print(repr(time_for_event))  # => datetime.timedelta(days=87,
# seconds=85080, microseconds=240064)

print(time_for_event)        # => 87 days, 23:38:00.240064
print(time_for_event.days)   # => 87

print(f"Faltam {time_for_event.days} dias e "
      f"{time_for_event.seconds // 3600} horas "
      f"para o aniversário do Osvaldo.")
# Saída: Faltam 87 dias e 23 horas para o aniversário
# do Osvaldo.

print(15*'-')

# -----------------------------------------------------------------

"""


import datetime

date_of_purchase = datetime.datetime.now()
print(f"date_of_purchase = {date_of_purchase}") # => date_of_purchase =
# 2024-07-09 17:34:59.037445

bill_rule = datetime.timedelta(days=3)
print(f"bill_rule = {bill_rule}")  # => bill_rule = 3 days,
# 0:00:00

bill_due_date = date_of_purchase + bill_rule
print(f"bill_due_date = {bill_due_date}") # => bill_due_date =
# 2024-07-12 17:34:59.037445

print(15*'-')