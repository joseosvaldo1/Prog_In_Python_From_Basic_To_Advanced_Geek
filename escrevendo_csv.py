"""
# Escrevendo em arquivos CSV:

- writer() (escritor) => Cria o objeto para que possamos escrever
arquivos .csv.
- writerow() => Possibilita escrever uma linha no arquivo .csv.

# -----------------------------------------------------------

# Usando o método writer():

# writer() => Gera um objeto que nos permite escrever
# em um arquivo .csv. Utilizamos o método writerow()
# do módulo csv para escrever cada linha do arquivo
# .csv. O método writerow() recebe como parâmetro uma
# lista.

from csv import writer

with open('movies.csv', 'w') as file:
	writer_csv = writer(file)
	movie = None
	writer_csv.writerow(['Title', 'Gender', 'Duration'])
	while movie != 'sair':
		movie = input('Enter a title for the movie: ')
		if movie != 'sair':
			gender = input('Enter a gender of the movie: ')
			duration = input('Enter a duration(min) of the movie: ')
			writer_csv.writerow([movie, gender, duration])


# -----------------------------------------------------------




# -----------------------------------------------------------



"""


# Usando o método DictWriter():

from csv import DictWriter

with open('movies_2.csv', 'w') as file:
	header = ['Title', 'Gender', 'Duration']
	writer_csv = DictWriter(file, fieldnames=header)
	writer_csv.writeheader()
	movie = None
	while movie != 'sair':
		movie = input('Enter a title for the movie: ')
		if movie != 'sair':
			gender = input('Enter a gender of the movie: ')
			duration = input('Enter a duration(min) of the movie: ')
			writer_csv.writerow({'Title': movie,
			                    'Gender': gender,
								'Duration': duration})


# Observação: As chaves do dicionário utilizadas em writerow()
# devem ser as mesmas que as utilizadas no cabeçalho.







