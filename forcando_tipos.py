"""
# Forçando Tipos de Dados Com Decorators:



"""


def force_types(*types):    # => Poderiamos usar o *args
	def decorator(function):
		def converts_types(*args, **kwargs):
			new_args = []
			for (value, type) in zip(args,types):
				new_args.append(type(value))
			return function(*new_args, **kwargs)
		return converts_types
	return decorator


@force_types(str, int)
def repeat_message(message,times):
	for time in range(times):
		print(message)

@force_types(float, float)
def divide(a, b):
	print(a/b)

print("repeat_message('Geek', '3'): ")
repeat_message('Geek', '3')
print(15*'-')

print("divide('1','5')")
divide('1','5')
print(15*'-')
