"""
##PEP8 - Python Enhancement Proposal:

-São propostas de melhorias para a linguagem Python.

# The Zen Of Python

import this

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious
way to do it.
Although that way may not be obvious at first unless you're
Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a
good idea.
Namespaces are one honking great idea -- let's do more
of those!

- A ideia da PEP8 é que possamos escrever códigos da
forma pythônica.
[1] Utilize o padrão Camel Case para o nome de classes;

# Exemplos de Nomes Para Classes em Python:

# Nome de classe de acordo com o PEP8


class Calculadora:
    pass

# Nome em desacordo com o PEP8
# class calculadora_científica:
    # pass

# Nome de acordo com o PEP8


class CalculadoraCientifica:
    pass

[2] Utilize letras minúsculas separadas por underline
para funções ou variáveis (padrão snake case);

# Exemplos de Nomes Para Funções em Python:


def soma():
    pass

def soma_dois():
    pass

# Exemplos de Nomes Para Variáveis em Python:

number = 4
odd_number = 5

[3] Utilize quatro espaços para identação de blocos;
if 'a' in 'banana':
    print ("tem")

[4] Linhas em Branco:
- Separar funções e definições de classe com duas linhas
em branco;
- Métodos dentro de uma classe devem ser separados por
uma única linha em branco;

class Classe:
    pass


class OutraClasse:
    pass


[5] imports
- Imports devem ser sempre feitos em linhas separadas

-import errado:
 import sys, os

 -import correto:
 import sys
 import os

 Observação: Não há problema em importar mais elementos
 em uma mesma linha, caso use o from:

 from types import StringType, ListType

 Observação: Caso tenha muitos import de um mesmo pacote,
 recomenda-se fazer:

 from types import (
    StringType,
    ListType,
    SetType,
    ...
 )

 - Import devem ser colocados no topo do arquivo - logo
 depois de quaisquer comentários ou docstrings e antes
 constantes e de variáveis globais.

 [6] Espaços em expressões e instruções:

 Não faça:
 def função (  algo[ 1 ], {  outro: 2  }  ):
    pass

 faça:
 def função (algo[1], {outro: 2}):
    pass

 Não faça:
 algo_(1)

 Faça:
 algo(1)

 Não faça:

 dict_['chave'] = lista_[indice]

 Faça:
 dict['chave'] = lista[indice]

 Não faça:
 x             = 1
 y             = 3
 variavel_long = 5

 Faça:
 x = 1
 y = 3
 variavel_long = 5

 [7] Termine sempre uma instrução com uma nova linha.

"""
import this










