"""
# O Bloco 'with':

- Passos para se trabalhar com arquivos:
1º Abrir o arquivo;
2º Manipaular o arquivo;
3º Fechar o arquivo.


- O bloco o 'with' é utilizado para criar um contexto de trabalho
onde os recursos utilizados são fechados após o bloco 'with'.

- O bloco 'with' em Python é uma estrutura que permite gerenciar o
contexto de execução de determinadas operações, como a abertura e
manipulação de arquivos ou a conexão e consulta a bancos de dados.
Ele garante que recursos sejam utilizados de forma segura e eficiente,
garantindo que sejam liberados automaticamente após sua utilização,
mesmo em caso de erros ou exceções.

- Ao usar o bloco 'with', você especifica um objeto que suporta o
protocolo de gerenciamento de contexto, geralmente utilizando o
método __enter__() para iniciar o contexto e o método __exit__()
para finalizá-lo. Dentro do bloco 'with', você pode realizar
operações com esse objeto de forma segura, e assim que o bloco
'with' for concluído, o contexto será encerrado automaticamente,
garantindo a liberação de recursos.

- Isso é particularmente útil ao lidar com recursos que precisam ser
fechados explicitamente, como arquivos abertos, conexões de banco de
dados ou conexões de rede. Em vez de usar um bloco 'try-finally' para
garantir a liberação desses recursos, o bloco 'with' simplifica o
código e torna mais claro o gerenciamento de contexto.

"""

# O bloco 'with' - forma pythonica de manipulação de arquivos.
with open('texto.txt') as file:
	print("Dentro do bloco 'with':")
	print(file.readlines())
	print(f"file,closed = {file.closed}")


print(20*'-')
print("Fora do bloco 'with':")
print(f"file.closed = {file.closed}")

#