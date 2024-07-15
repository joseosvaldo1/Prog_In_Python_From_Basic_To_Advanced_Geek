"""
# Introdução ao módulo Unittest:

- Unitest => testes unitários.
- O que são testes unitários?
	* Teste unitário é a forma de se testar unidades inividuais
	de código fonte.
	* Unidades individuais de código fonte podem ser: funções,
	métodos, classes, módulos, etc.

- Observação: Teste unitário não é específico da linguagem
Python.

- Pata criar nossos testes, criamos classes que herdam de
unittest.TestCase e, a partir de então, ganhamos todos os
assertions presentes no módulo.

- Para rodar todos os testes, utilizamos unittest.main().

- TestCase => Casos de teste para sua unidade de código.

# -----------------------------------------------------------------

- Conhecendo os assertions do Unittest:

Método ----------------------------- Checa se:
assertEqual(a, b) ------------------ a == b
assertNotEqual(a, b) --------------- a != b
assertTrue(x) ---------------------- bool(x) = True
assertFalse(x) --------------------- bool(x) = False
assertIs(a, b) --------------------- a é(is) b
assertIsNot(a, b) ------------------ a não é (is not) b
assertIsNone(x) -------------------- x é(is) None
assertIsNotNone(x) ----------------- x não é (is not) None
assertIn(a, b) --------------------- a in b (a está contido em b)
assertNotIn(a, b) ------------------ a not in b (a não está contido em b)
assertIsInstance(a, b) ------------- a é instância de b -
									 isinstance(a, b)
assertNotIsInstance(a, b) ---------- a não é instância de b -
									 not isinstance(a, b)

Link: https://docs.python.org/3/library/unittest.html

# -----------------------------------------------------------------

- Por convenção, todos os testes em um test case devem ter seus
nomes iniciados por test_

- Para executar os testes com unittest sem detalhamento:
python nome_do_modulo.py

- Para executar os testes com unittests com detalhamento:
python nome_do_modulo.py -v

- Docstrings nos testes:
- Podemos acrescentar (e é recomendado) docstrings nos nossos
testes.



"""

# Prática - Utilizando a abordagem TDD:



