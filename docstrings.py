"""
# Documento Funções com Docstrings:

Observações:

1) Podemos ter acesso a documentação de uma função em Python
usando a propriedade especial __doc__: nome_da_função.__doc__

2) Podemos ainda fazer um acesso a documentação de uma função
usando a função 'help()'.
"""


# Exemplos:
# Exemplo_1:

def diz_oi():
	""" Uma função simples que retorna apenas a string 'Oi!'. """
	return 'Oi!'


# Exemplo_2:

def exponencial(base, exponente=2):
	"""

	Função que retorna por padrão o quadrado de um numero - base
	ou retorna a base elevado ao expoente informado.
	:param base: Número que será elevado a base
	:param exponente: Número que será o expoente da exponenciação.
	Por padrão é o número 2.
	:return Retorna a base elevada ao exponente.

	base**expoente
	"""

	return base ** exponente

