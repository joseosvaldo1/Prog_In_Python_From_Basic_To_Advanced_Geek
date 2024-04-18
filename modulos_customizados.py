"""
# Módulos Customizados:

- Como módulos Python nada mais são do arquivos em Python, então
TODOS os arquivos que criamos neste curso são módulos Python
prontos para serem utilizados.


# -----------------------------------------------

# Importando uma função específica do nosso módulo
# funcoes_com_parametors:

from funcoes_com_parametros import soma_impares

print(f"soma_impares = {soma_impares([1, 2, 3, 4, 5, 6, 7, 8, 9])}")
# Saída: soma_impares = 25

# -------------------------------------------------

# Importada t o d o o módulo:
# Nesse caso, teremos acesso a todos os elementos do módulo

import funcoes_com_parametros as fcp

# Acessando duas variáveis (list_1 e tuple_1) contida no módulo:
print(f"list_1 = {fcp.list_1}")
# Saída: list_1 = [1, 2, 3, 4, 5, 6, 7]
print(15*'-')
print(f"tuple_1 = {fcp.tuple_1}")
print(15*'-')
print(f"fcp.soma_impares(fcp.list_1) = {fcp.soma_impares(fcp.list_1)}")
print(15*'-')

# -----------------------------------------

"""

from map import cities_tempratures_c, celsius_para_fahrenheit

print(15*'-')
print(list(map(celsius_para_fahrenheit, cities_tempratures_c)))
print(15*'-')