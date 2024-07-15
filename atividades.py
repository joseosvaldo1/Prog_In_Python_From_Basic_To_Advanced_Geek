def eat(food, its_healthy):
	if its_healthy:
		final = 'because I want to stay in shape'
	else:
		final = 'because you only live once'

	return f"I'm eating {food} {final}."


def sleep(number_of_hours):
	if number_of_hours > 8:
		return f"Putz! I slept a lot. I'm late for work."
	else:
		return (f"I'm still tired after sleeping "
		        f"for {number_of_hours} hours. :(")
