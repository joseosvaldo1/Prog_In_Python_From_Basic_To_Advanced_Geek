"""
# Unittest - antes e após hooks:


- Hooks => São os testes em si, ou seja, a execução dos testes.

- Para realizar algo antes e depois do testes, o módulo
unittest tem dois métodos:

	* setUp() => É executado antes de cada método de teste.
	É útil para criarmos instâncias de objetos e outros
	dados.

	* tearDown() => É executado ao final de cada método de
	teste. É útil para excluir ou fechar conexões com bancos
	de dados.

# --------------------------------------------------------


"""

import unittest


class ModuloTest(unittest.TestCase):
	def setUp(self):
		# Configuações do setUp():
		pass

	def test_primeiro(self):
		# setUp será executado antes do teste.
		# tearDown será executado após o teste.
		pass

	def test_segundo(self):
		# setUp será executado antes do teste.
		# tearDown será executado após o teste.
		pass

	def tearDown(self):
		# Configuações do tearDown():
		pass
	