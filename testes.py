import unittest

from atividades import eat, sleep, its_funny


class AtividadesTestes(unittest.TestCase):
	def test_eat_healthy(self):
		"""Testing the return with healthy food."""
		self.assertEqual(
			eat('okra', True),
			"I'm eating okra because I want to stay in shape."
		)

	def test_eat_delicious(self):
		"""Testing the return without healthy food."""
		self.assertEqual(
			eat(food='pizza', its_healthy=False),
			"I'm eating pizza because you only live once."
		)

	def test_sleep_a_bit(self):
		"Testing the return with number_of_hours < 8."
		self.assertEqual(
			sleep(4),
			"I'm still tired after sleeping for 4 hours. :("
		)

	def test_sleep_a_lot(self):
		"Testing the return with number_of_hours > 8."
		self.assertEqual(
			sleep(10),
			"Putz! I slept a lot. I'm late for work."
		)

	def test_its_funny(self):

		self.assertEqual(
			its_funny('Sergio Malandro'), False
		)
		self.assertFalse(
			its_funny('Sergio Malandro')
		)

		self.assertTrue(
			its_funny('Jim Carrey'),
			"Jim Carrie should be funny!"

		)



if __name__ == '__main__':
	unittest.main()

# Observação: Por convenção, todos os testes em um test case
# devem ter seus nomes iniciados por test_.
