"""
# Lendo Arquivos CVS:

- CSV => Comma Separated Values - Valores Separados por Vírgulas.

- Podemos ter outros tipos de separadores além das vírgulas.

Exemplos:
1) Separados por vírgulas:
1, 2, 3, 4, 5, 6
'Geek', 'University', 'Python', 'Ciencia', 'Dados

2) Saparados por ponto e vírgula:
1; 2; 3; 4; 5; 6
'Geek'; 'University'; 'Python'; 'Ciencia'; 'Dados

3) Separados por espaço:
1 2 3 4 5 6
'Geek' 'University' 'Python' 'Ciencia' 'Dados

- Site para obtenção de dados: https://dados.gov.br/dataset

# ----------------------------------------------------------

# Forma possível de se trabalhar, mas não é o ideal (trabalhoso):

with open('lutadores.csv') as file:
	data = file.read()
	# print(f"type(data) = {type(data)}")  # => type(data) = <class 'str'>
	print(15 * '-')
	print('Data(dados):')
	print(15*'-')
	print(" ")
	print(data)
	print(15 * '-')
	print(data.split(','))     # => Com o cabeçalho do CSV
	print(data.split(',')[3:]) # => Sem o cabeçalho do CSV
	print(15 * '-')


# ----------------------------------------------------------

- A linguagem Python possui duas formas diferentes para ler
dados em arquivos do tipo CSV:
	* Reader => Permite que iteremos sobre as linhas do
	arquivo CSV como listas;
	* DictReader => Permite que iteremos sobre as linhas do
	arquivo CSV como OrderedDict;

# -------------------------------------------------------------


# 1st way - Using Reader Module:

from csv import reader

with open('lutadores.csv') as file:
	reader_csv = reader(file)  # => reader_csv is an iterator
	print(type(reader_csv))    # => <class '_csv.reader'>
	next(reader_csv)           # => we skip the header
	for line in reader_csv:
		# Each line is a list.
		print(f"{line[0]} was born in {line[1]} "
		      f"e his/her height is {line[2]}.")


# Saída:

# <class '_csv.reader'>
# Ryu was born in Japao e his/her height is 175.
# Ken was born in EUA e his/her height is 175.
# Chun-Li was born in China e his/her height is 165.
# Guile was born in EUA e his/her height is 185.
# E. Honda was born in Japao e his/her height is 175.
# Dhalsim was born in India e his/her height is 176.
# Blanka was born in Brasil e his/her height is 192.
# Zangief was born in Russia e his/her height is 214.


# ----------------------------------------------------------

# 2nd way - Using DictReader Module:

# Utilizando a vírgula como separador:
from csv import DictReader

with open('lutadores.csv') as file:
	reader_csv = DictReader(file)  # => reader_csv is an iterator
	print(type(reader_csv))        # => <class '_csv.reader'>
	for line in reader_csv:
		# Each line is a OrderedDict.
		print(f"{line['Nome']} was born in {line['Pais']} "
		      f"and his/her height {line['Altura (em cm)']}.")

# -----------------------------------------------

- Conteúdo do arquivo lutadores.csv:

Nome;Pais;Altura (em cm)
Ryu;Japao;175
Ken;EUA;175
Chun-Li;China;165
Guile;EUA;185
E. Honda;Japao;175
Dhalsim;India;176
Blanka;Brasil;192
Zangief;Russia;214

"""

# 2nd way - Using DictReader Module:

# Usando DictReader com outro tipo de separador:
from csv import DictReader

with open('lutadores.csv') as file:
	reader_csv = DictReader(file, delimiter=';')  # => reader_csv is an iterator
	print(type(reader_csv))        # => <class '_csv.reader'>
	for line in reader_csv:
		# Each line is a OrderedDict.
		print(f"{line['Nome']} was born in {line['Pais']} "
		      f"and his/her height {line['Altura (em cm)']}.")

