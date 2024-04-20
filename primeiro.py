
def function1():
	print("Geek University - primeiro.py")

if __name__ == "__main__":
	function1()
	print("primeiro.py está sendo executado diretamente!")
else:
	print(f"primeiro.py foi importado com sucesso!=> "
		  f"__name__ = {__name__}")