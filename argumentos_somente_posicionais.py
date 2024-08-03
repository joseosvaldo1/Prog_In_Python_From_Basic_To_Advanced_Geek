"""
# Novos Recursos do Python:
- Argumentos somente posicionais:

- Em Python, os argumentos somente posicionais são aqueles que devem ser
fornecidos apenas por posição, não por nome. Isso é útil para garantir que
certas funções sejam chamadas de maneira previsível e evitar erros ao passar
argumentos.

### Como definir argumentos somente posicionais

- A partir do Python 3.8, você pode definir argumentos somente posicionais
usando o símbolo `/` em uma definição de função. Os argumentos listados antes
do `/` são somente posicionais, o que significa que eles não podem ser passados
como argumentos nomeados ao chamar a função.

### Exemplo de argumentos somente posicionais

- Aqui está um exemplo que demonstra como definir e usar argumentos somente
posicionais:


def minha_funcao(a, b, /, c, d):
    print(f"a = {a}, b = {b}, c = {c}, d = {d}")

# Chamadas válidas:
minha_funcao(1, 2, 3, 4)          # a = 1, b = 2, c = 3, d = 4
minha_funcao(1, 2, c=3, d=4)      # a = 1, b = 2, c = 3, d = 4

# Chamadas inválidas que resultam em TypeError:
minha_funcao(a=1, b=2, c=3, d=4)  # TypeError: minha_funcao() got some
positional-only arguments passed as keyword arguments: 'a, b'
minha_funcao(1, b=2, c=3, d=4)    # TypeError: minha_funcao() got some
positional-only arguments passed as keyword arguments: 'b'


### Explicação do Exemplo

- Na função `minha_funcao`, os argumentos `a` e `b` são definidos como somente
posicionais pelo uso do `/`.
- Os argumentos `c` e `d` podem ser passados por posição ou como argumentos
nomeados.
- Chamadas como `minha_funcao(a=1, b=2, c=3, d=4)` são inválidas porque `a` e
`b` devem ser fornecidos por posição.

### Uso e Benefícios

1. **Interface de Função Claramente Definida**: Ajuda a manter a interface
da função clara e previsível.
2. **Retrocompatibilidade**: Facilita a manutenção de retrocompatibilidade
ao adicionar novos parâmetros nomeados.

3. **Desempenho**:
- Pode melhorar o desempenho ao evitar a sobrecarga de
resolução de argumentos nomeados.

### Considerações Adicionais

- Os argumentos posicionais são seguidos por argumentos que podem ser
posicionais ou nomeados, e depois por argumentos nomeados, se houver.
- A sintaxe `/` é útil em bibliotecas e APIs públicas para garantir que
certos parâmetros críticos sejam passados corretamente.

- Aqui está um exemplo mais avançado com a combinação de argumentos posicionais,
posicionais ou nomeados, e somente nomeados:


def funcao_avancada(a, b, /, c, d, *, e, f):
    print(f"a = {a}, b = {b}, c = {c}, d = {d}, e = {e}, f = {f}")

# Chamadas válidas:
funcao_avancada(1, 2, 3, 4, e=5, f=6)  # a = 1, b = 2, c = 3, d = 4,
e = 5, f = 6
funcao_avancada(1, 2, c=3, d=4, e=5, f=6)  # a = 1, b = 2, c = 3, d = 4,
e = 5, f = 6

# Chamadas inválidas que resultam em TypeError:
funcao_avancada(a=1, b=2, c=3, d=4, e=5, f=6)  # TypeError
funcao_avancada(1, 2, 3, 4, 5, 6)  # TypeError: funcao_avancada() takes
4 positional arguments but 6 were given


No exemplo acima, `a` e `b` são somente posicionais, `c` e `d` podem ser
posicionais ou nomeados, e `e` e `f` são somente nomeados.


# ----------------------------------------------------------------------

def greet_v1(name: str) -> str:
	return f"Hi, {name}!"


print(f"greet_v1('Geek'): {greet_v1('Geek')}")  # => greet_v1('Geek'):
# Hi, Geek!
print(15*'-')

print(f"greet_v1(name='Geek'): {greet_v1(name='Geek')}")  # => greet_v1(
# name='Geek'): Hi, Geek!
print(15*'-')

def greet_v2(name: str, /) -> str:
	return f"Hi, {name}!"


print(f"greet_v2('Geek'): {greet_v2('Geek')}")  # => greet_v1('Geek'):
# Hi, Geek!
print(15*'-')

# print(f"greet_v2(name='Geek'): {greet_v2(name='Geek')}")  # => TypeError:
# greet_v2() got some positional-only arguments passed as keyword arguments:
# 'name'
# print(15*'-')


# ----------------------------------------------------------------------


def greet_v3(name: str, /, mesage: str = "Hi") -> str:
	return f"{mesage}, {name}!"


print(greet_v3('Geek'))

print(15*'-')

print(greet_v3('University', mesage="Hello"))

print(15*'-')

print(greet_v3('Felicity', 'Welcome'))

print(15*'-')


# -------------------------------------------------------------


def greet_v4(name: str, mesage: str = "Hi", /) -> str:
	return f"{mesage}, {name}!"


print(greet_v4('Geek'))

print(15*'-')

print(greet_v4('Felicity', 'Welcome'))

print(15*'-')

# print(greet_v4('University', mesage="Hello"))  # => TypeError:
# greet_v4() got some positional-only arguments passed as keyword
# arguments: 'mesage'

# print(15*'-')


# ------------------------------------------------------------------

# Assim como temos os argumento somente posicionais (os argumentos
# anteriores a /), temos também os argumentos somente nomeados
# (todos os argumentos que vierem após o asterisco *).

def greet_v5(*, name: str) -> str:
	return f"Hi, {name}!"


print(greet_v5(name='Geek'))

print(15*'-')

# print(greet_v5('Geek'))  # => TypeError: greet_v5() takes 0
# positional arguments but 1 was given


# ------------------------------------------------------------------



"""


def greet_v6(name: str, /, mesage1: str = "Hi", *, mesage2: str) -> str:
	return f"{mesage1}, {name}! {mesage2}."


print(greet_v6('Geek', mesage1="Hello", mesage2="Have a good day"))

print(15*'-')

print(greet_v6('Geek', mesage2="Have a good day"))

print(15*'-')

# print(greet_v6('Geek', 'Oi', 'Letś go!'))  # => TypeError:
# greet_v6() takes from 1 to 2 positional arguments but 3 were given

# print(15*'-')









