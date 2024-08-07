"""
# Novos Recursos do Python:
* Alerta Sobre Sintaxes Perigosas:

- Em Python, a biblioteca warnings permite emitir avisos que indicam
possíveis problemas no código que não são graves o suficiente para
interromper a execução, mas que podem levar a erros ou comportamentos
inesperados. Avisos (warnings) são frequentemente usados para alertar
sobre a depreciação de funcionalidades, práticas de codificação
questionáveis, ou outras condições potencialmente problemáticas.


* Conceitos que causam confusão nos desenvolvedores:

== => É usado para checar valores;

is => É usado se os objetos são os mesmos.

# >>> versao = '3.8'
# >>> versao
'3.8'
# >>> versao is '3.8'
<stdin>:1: SyntaxWarning: "is" with 'str' literal. Did you mean "=="?
False
# >>> versao == '3.8'
True
# >>>

# ------------------------------------------------------------------


# >>> list_str = [
... ('Geek')
... ('University')
... ]
<stdin>:2: SyntaxWarning: 'str' object is not callable; perhaps you
missed a comma?
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: 'str' object is not callable
# >>>

# ------------------------------------------------------------------



"""