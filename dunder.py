"""
# Dunder Name e Dunder Main:

- Dunder => Double Under (__);
- Dunder Name => __name__
- Dunder Main => __main__

- Métodos Dunder Integrados iniciais no Python:

(guppe) jose@jose:~/PycharmProjects/guppe/guppe/
Prog_In_Python_From_Basic_To_Advanced_Geek$ python
Python 3.12.1 (main, Jan  6 2024, 12:09:57) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
# >>> dir()
# ['__annotations__', '__builtins__', '__doc__', '__loader__',
# '__name__', '__package__', '__spec__']
# >>>


# ------------------------------------------------------------

- Os métodos Dunder, também conhecidos como métodos mágicos, são
métodos especiais no Python que são chamados automaticamente em
determinadas situações. Eles são nomeados com dois sublinhados
antes e depois do nome do método, como __name__ e __main__.

* Método __name__:

- O método __name__ retorna o nome do módulo atual. Ele é útil para
verificar se o script está sendo executado como um módulo ou como
um script autônomo.

Exemplo:

# modulo.py
print(__name__)  # Saída: modulo
# script.py
import modulo
print(modulo.__name__)  # Saída: modulo
print(__name__)  # Saída: __main__

* Método __main__:

- O método __main__ é executado quando o script é executado como
um script autônomo. Ele contém o código principal que deve ser
executado.

Exemplo:

# script.py
if __name__ == "__main__":
    # Código principal aqui
- Quando o script script.py é executado, o método __main__ será executado.
No entanto, se script.py for importado como um módulo, o método __main__
não será executado.

* Outros Métodos Dunder:

Além de __name__ e __main__, existem vários outros métodos Dunder no
Python, incluindo:

__init__: Construtor de classe
__str__: Método de representação de string
__repr__: Método de representação de depuração
__add__: Operador de adição
__len__: Operador de comprimento

- Os métodos Dunder são uma parte poderosa da linguagem Python e podem
ser usados para vários propósitos, como manipulação de objetos, controle
de fluxo e muito mais.


# ------------------------------------------------------------
- A comunidade Python utiliza esses Dunder como funções, atributos
ou propriedades internas da linguagem para que eles não conflitem
com nomes de variáveis geradas pelos programadores.

- Em Python, são utilizandos métodos dunder para que criar funções,
atributos, propriedades internas, etc. utilizando double under (__)
para não gerar conflitos com os nomes desses elementos na
programação.


# ------------------------------------------------------------
Por que main e name:

- Na linguagem C, teremos um programa da seguinte forma:

int main(){
	<código>
	return 0
}

- Na linguagem Java, teremos um programa da seguinte forma:


public static void (String[] args){
	<código>
}

- Em Python, se executarmos um módulo Python diretamente na
linha de comando, internamente o interpretador Python atribuirá
à variável __name__ o valor __main__ indicando que este módulo
é o módulo de execução principal.

(guppe) jose@jose:~/PycharmProjects/guppe/guppe/Prog_In_Python_From_Basic_To_Advanced_Geek$ python
Python 3.12.1 (main, Jan  6 2024, 12:09:57) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
# >>> dir()
# ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
# '__package__', '__spec__']
# >>> print(__name__)
# __main__
# >>>

# ------------------------------------------------------------

from funcoes_com_parametros import soma_impares

print(20*'-')
print(soma_impares([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(20*'-')


# ------------------------------------------------------------

# main => Significa "Principal".

Observação: Quando um arquivo Python é executado diretamente, ou seja,
como um script principal, o Python define automaticamente o atributo
__name__ do módulo atual como __main__. Isso permite que você identifique
quando um módulo está sendo executado como o programa principal.Por outro
lado, se esse mesmo arquivo Python for importado como um módulo em outro
arquivo, o Python define o atributo __name__ como o nome real do arquivo,
sem a extensão .py. Isso ocorre para diferenciar quando o arquivo está
sendo importado como um módulo em vez de ser executado diretamente.Essa
diferenciação é útil em situações onde você deseja ter comportamentos
diferentes dependendo de como o arquivo está sendo utilizado. Por exemplo,
você pode ter código que só é executado quando o arquivo é o script
principal, mas não quando é importado como um módulo. Isso é comumente
utilizado em testes unitários e em blocos de código que são destinados
exclusivamente para execução direta.

"""

import primeiro
import segundo
