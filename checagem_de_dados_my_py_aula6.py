"""
# Checagem de tipos em Python:
# Aula 5 - Checagem de Tipos com MyPy:

Link do site do MyPy: https://mypy-lang.org/

- MyPy é uma ferramenta de verificação estática de tipos para Python.
Ele permite que você adicione anotações de tipo ao seu código Python
e, em seguida, verifica essas anotações para garantir que seu código
está usando os tipos corretamente. Embora Python seja uma linguagem
dinamicamente tipada, MyPy permite que você obtenha alguns dos
benefícios da verificação de tipos estática, como a detecção precoce
de erros de tipo, melhor documentação e suporte para ferramentas de
desenvolvimento.

- Principais Características do MyPy:

1) Verificação Estática de Tipos:
    MyPy analisa o código Python anotado com dicas de tipo
    (type hints) e verifica se os tipos são usados corretamente,
    sem executar o código.

2) Suporte para Python Dinâmico:
    MyPy é projetado para trabalhar bem com o estilo dinâmico do
    Python. Você pode introduzir gradualmente as anotações de tipo
    em seu código existente.

3) Integração com IDEs:
    Muitas IDEs e editores de texto, como PyCharm e Visual Studio Code,
    suportam MyPy, fornecendo feedback imediato sobre erros de tipo.

4) Compatibilidade com Tipos do Python:
    MyPy suporta totalmente os tipos introduzidos nas versões mais
    recentes do Python, incluindo tipos genéricos, TypedDict,
    Protocol, entre outros.

- Como Usar o MyPy:

    Instalação:
    Você pode instalar o MyPy usando o pip:

sh
	pip install mypy

	Anotar seu Código:
	Adicione anotações de tipo ao seu código. Por exemplo:

Pyhton code:

def sgreet(name: str) -> str:
    return f"Hi, {nome}!"

Executar o MyPy:
Execute MyPy no seu código para verificar as anotações de tipo:

sh:
    mypy seu_arquivo.py

Exemplo de Uso do MyPy:

Considere o seguinte código anotado:

Python Code:

from typing import List

def sum_elements(numbers: List[int]) -> int:
    return sum(numbers)

numbers = [1, 2, 3]
resul = sum_elements(numbers)
print(result)

Se você alterar numbers para conter strings:

Python Code:

numbers = ["1", "2", "3"]
result = sum_elements(numbers)
print(result)

Executando MyPy neste código resultará em um erro de tipo:

sh:

$ mypy seu_arquivo.py
seu_arquivo.py:9: error: List item 0 has incompatible type "str";
expected "int"

- Benefícios do MyPy:

1) Detecção Precoce de Erros: Encontra erros de tipo antes da execução
do código.

2) Documentação Melhorada: As anotações de tipo servem como
documentação para desenvolvedores, tornando o código mais legível e
compreensível.

3) Ferramentas de Desenvolvimento: Ferramentas como linters e IDEs
podem usar informações de tipo para fornecer autocompletar,
refatoração e outras funcionalidades avançadas.

- MyPy é uma ferramenta poderosa para desenvolvedores Python que
desejam adicionar verificação de tipos estática ao seu fluxo de
trabalho, ajudando a manter a qualidade e a robustez do código.



"""


def header(text: str, alignment: bool = True) -> str:
    if alignment:
        return f"{text.title()}\n{'-'*len(text)}"
    else:
        return f"{text.title()}".center(50, '#')


print(header(text='Geek University'))

print(30*'-')

print(header(text='Geek University', alignment=False))

print(30*'-')

print(header(text='Geek University', alignment=True))

