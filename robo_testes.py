import unittest

from robo import Robot

class RoboTestes(unittest.TestCase):

	def setUp(self):
		self.megaman = Robot('Mega Man', battery=50)
		print('setUp method is being executed...')

	def test_charge(self):
		self.megaman.charge()
		self.assertEqual(self.megaman.batery, 100)

	def test_say_name(self):
		self.assertEqual(self.megaman.say_name(),
		                 'BEEP BOOP BEEP BOOP. '
		                 'EU SOU MEGA MAN')

		self.assertEqual(self.megaman.batery, 49,
		                 'The battery should be at 49 percent!')

	def tearDown(self):
		print('tearDown() method is being executed...')

if __name__ == '__main__':
	unittest.main()