"""
# Trabalhando Com Módulos Externos:

- Utilizamos o gerenciador de pacotes Python chmado 'pip'.
- pip => Python Installer Package
- Podemos conhecer todos os pacotes externos Python
oficiais em: https://pypi.org

- Colorama => É utilizado para permitir a impressão de textos
coloridos no terminal.

# -----------------------------------------

# Instalando o pacote colorama (uso de terminal):

pip install colorama

# -----------------------------------------

# Utilizando o pacote colorama instalado:

from colorama import init, Fore, Back, Style
init()
print(Fore.MAGENTA + 'Geek University')
print(Fore.CYAN + 'Geek University')
print(Fore.WHITE + 'Geek University')

# -----------------------------------------

# Instalando o pacote pypdf (via terminal):

pip install python-pdf

# -----------------------------------------

# Utilizando o pacote pydf:

import pydf

pdf = pydf.generate_pdf('<h1>Geek University</h1>')
with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)

"""

import pydf

pdf = pydf.generate_pdf('<h1>Geek University</h1>'
                        '<br/><br/>'
                        '<strong>Python Programming Essential</strong>')
with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)







