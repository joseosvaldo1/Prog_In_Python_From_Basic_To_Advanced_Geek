"""
# Checagem de Tipos em Python:
# Aula 4 - Type Hiting:

- Type hinting (ou dicas de tipo) em Python é uma maneira de
especificar os tipos de variáveis, parâmetros de funções e
valores de retorno de funções. Embora Python seja uma linguagem
dinamicamente tipada, o type hinting fornece uma maneira de
documentar e verificar tipos de dados usando anotações, melhorando
a legibilidade do código e ajudando ferramentas como linters e IDEs
a detectar erros de tipo.

Exemplo Básico:

def saudacao(nome: str) -> str:
    return f"Olá, {nome}!"

print(saudacao("João"))  # Saída: Olá, João!

Neste exemplo:

    nome: str indica que o parâmetro nome deve ser
    uma string. -> str indica que a função retorna uma string.

- Exemplo com Variáveis:

idade: int = 30
nome: str = "Maria"

Aqui, idade é anotada como um inteiro e nome como uma string.
Exemplo com Tipos Compostos:

O módulo typing fornece vários tipos compostos que podem ser usados
para anotações mais complexas.

- Listas e Dicionários:

from typing import List, Dict

numeros: List[int] = [1, 2, 3, 4]
notas: Dict[str, float] = {"Matemática": 9.5,
                           "História": 8.0}

Tuplas e Conjuntos:

from typing import Tuple, Set

coordenadas: Tuple[int, int] = (10, 20)
frutas: Set[str] = {"maçã", "banana", "laranja"}

Exemplo com Funções Complexas:

python

from typing import Callable

def executar(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

def soma(x: int, y: int) -> int:
    return x + y

print(executar(soma, 5, 3))  # Saída: 8

Neste exemplo, Callable[[int, int], int] indica que func deve ser uma
função que recebe dois inteiros e retorna um inteiro.

- Benefícios do Type Hinting:

* Documentação: Ajuda a entender rapidamente o que a função espera e
retorna. Verificação de Erros: Ferramentas como mypy podem verificar
inconsistências de tipo.

* Autocompletar e Análises Estáticas: IDEs podem fornecer sugestões
melhores e detectar problemas antes da execução.

Embora as dicas de tipo não sejam obrigatórias e não alterem o
comportamento em tempo de execução, elas são extremamente úteis
para manter e desenvolver código de alta qualidade.


"""


def greet(name: str) -> str:
    return f"Hi, {name}!"


print(greet('Geek'))
# print(greet(1))


def header(text: str, alignment: bool = True) -> str:
    if alignment:
        return f"{text.title()}\n{'-'*len(text)}"
    else:
        return f"{text.title()}".center(50, '#')


print(header(text='Geek University'))
print(header(text='Geek University', alignment=False))

# Observação: Mesmo que a gente explicite os tipos de dados
# dos parâmetros e do retorno, isso não irá fazer com o que
# o programa seja executado forma incorreta.

print(header(text='Geek University', alignment='Geek'))
