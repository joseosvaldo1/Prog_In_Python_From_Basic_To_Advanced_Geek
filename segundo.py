import primeiro

def function2():
	primeiro.function1()

if __name__ == "__main__":
	function2()
	print("segundo.py está sendo executado diretamente!")
else:
	print(f"segundo.py foi importado com sucesso! =>"
		  f"__name__ = {__name__}")