class Robot:
	def __init__(self, name, battery=100, abilities=[]):
		self.__name = name
		self.__battery = battery
		self.__abilities = abilities

	@property
	def name(self):
		return self.__name

	@property
	def batery(self):
		return self.__battery

	@property
	def abilities(self):
		return self.__abilities

	def charge(self):
		self.__battery = 100



	def say_name(self):
		if self.__battery > 0:
			self.__battery -= 1
			return (f'BEEP BOOP BEEP BOOP. EU SOU '
			        f'{self.__name.upper()}')

		return (f'Low battery! Please recharge the battery and'
		        f'try again!')


	def learn_ability(self, new_ability, cost):
		if self.__battery >= cost:
			self.__battery -= cost
			self.__abilities.append(new_ability)

			return (f"Wow, EU APRENDI A NEW ABILITY: "
		            f"{new_ability.upper()}")

		return (f'Insufficient battery! Please recharge the '
		        f'battery and try again!')