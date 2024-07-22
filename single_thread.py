"""
# GIL- Python Global Interpreter Lock:

	O Python Global Interpreter Lock, ou simplesmente GIL, é um mutex
(ou lock) que permite que apenas uma thread tome conta do interpretador
Python.
	Isso significa que somente uma thread pode estar em um estado de
execução em qualquer ponto do tempo.
	O impacto do GIL não é comumente visível para desenvolvedores que
executam programas single-thread, mas pode ser uma dor de cabeça para
programas que precisam de tempo de resposta em códigos multi-thread.
Desde que o GIL permite apenas uma thread a ser executada, mesmo em
computadores multi- threads com arquitetura que permite utilizar mais
de um CPU ou core, o GIL tem ganhado reputação como um recurso
'indecente' do Python.
	Nesta aula, iremos aprender como o GIL afeta a performance do seu
programa Python e também como a gente pode mitigar (diminuir) o impacto
no nosso código.
	Como vimos na aula passada, Python utiliza reference counting para
gerenciamento de memória.
	Isso significa que para cada objeto criado Python mantém uma variável
de contagem de referência que guarda quantas referências apontam para o
objeto. Quando o contador de referências chega a zero, a memória ocupada
é liberada

No terminal:
#  import sys           - No código ao lado, a contagem de
#  a = []               referências deu 3.
#  b = a                - O objeto lista foi referenciado por
#  sys.getrefcount(a)   'a', por 'b' e pelo argumento passado
#                          ao sys.getrefcount().

	O problema é que essa forma de gerenciamento de memória utilizando
reference couting precisa de proteção para um fenômeno chamado 'race
conditions', onde duas threads aumentam ou diminuem seu valor
simultaneamente.
	Se isso acontecer, poderá causar problemas de memória que nunca é
liberada, ou ainda pior, liberação incorreta de memória enquanto ainda
existe referência para o objeto.
	E isso pode causar 'crashs' ou outros bugs esquisitos no seu
programa Python.
	Este reference couting pode ser mantido seguro adicionando 'locks'
em toda estrutura de dados que são compartilhadas via threads. Desta
forma eles não são modificados de forma inconsistente.
	O problema é que adicionar 'locks' em cada objeto ou grupo de objetos
significa que múltiplos locks irão existir, e isso irá causar um outro
problema - Deadlocks (deadlocks só podem existir se existe mais de um
lock). Outro efeito colateral seria decaimento da performance causada
pela repetida aquisição e liberação dos locks.
	O GIL aplica na regra de execução de qualquer código Python o single
lock previnindo qualquer deadlock, o que por outro lado transforma
qualquer código Python em single-thread. Vale mencionar que o GIL apesar
de ser usado também em outras linguagens de programação, como Ruby, não
é a única solução.
	Algumas linguagens evitam o uso do GIL para gerenciamento de memória
em thread utilizando abordagens diferentes do reference counting que
o Python utiliza. Por exemplo, uma das abordagens que outras linguagens
utilizam é o compilador JIT - Just inTime, como o Java.

"""


# Exemplo_1 - single thread:

import time
from threading import Thread

COUNTER = 50000000


def time_countdown(n):
	while n > 0:
		n -= 1


start = time.time()
time_countdown(COUNTER)
end = time.time()

print(f"Time interval in s - single thread: "
      f"{end - start} s.") # => Time interval in s -
# single thread:  8.296652793884277 s.









