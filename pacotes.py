"""
# Pacotes:

- Diferença entre pacote e módulo:

* Módulo => É apenas um arquivo Python que pode ter diversas
funções para utilizarmos.
* Pacote => É um diretório contendo uma coleção de módulos.

Observações:
1) Nas versões 2.x do Python, um pacote Python deveria
conter dentro dele um arquivo chamado __init__.py.
2) Nas versões 3.x do Python, não é mais obrigatória a presença
do arquivo __init__.py, mas normalmente é utilizado para
manter a compatibilidade.

# ------------------------------------------------------

from geek import geek1, geek2
from geek.university import geek3, geek4

print(f"geek1.pi = {geek1.pi}")
print(15*'-')
print(f"geek1.function1(4,6) = {geek1.function1(4, 6)}")
print(15*'-')
print(f"geek2.function2() = {geek2.function2()}")
print(15*'-')
print(f"geek3.function3() = {geek3.function3()}")
print(15*'-')
print(f"geek4.function() = {geek4.function4()}")
print(15*'-')

# ------------------------------------------------------



"""

from geek.geek1 import function1
from geek.university.geek4 import function4

print(f"function1(6,9) = {function1(6, 9)}")
print(15*'-')
print(f"function4() = {function4()}")