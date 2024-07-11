"""
# Por que testar nosso código?:

- Testamos nosso código para verificar se ele se comporta
e funciona da forma como esperamos.

- Razões para realizar testes:
	* Reduzir bugs (problemas) no código existente;
	* Testes garantem que novos recursos da sua aplicação
	não quebrem (alterem) recursos antigos;
	* Testes garantem que bugs (problemas) que foram corrigidos
	anteriormente continuam corrigidos;
	* Testes garantem que a refatoração que costumamos fazer
	não tragam novos bugs (problemas).


- TDD = Test Driven Development (Desenvolvimento Guiado por Testes) =>
Vertente de teste de código mais utilizada atualmente. Nessa vertente,
primeiro escrevem-se testes e após isso, o código propriamente dito.

- Com TDD é utilizado estágios de desenvolvimento:
	* Escreve-se o teste primeiro;
	* Depois, escreve-se o código mínimo suficiente para
	fazer o teste passar (ou seja, executar com sucesso);
	* Em seguida, refatora - se o código para realizar a
	funcionalidade e testa-se novamente o código refatorado;
	* Por último, uma vez que o teste passe, o recurso é
	considerado completo.

- Estes estágios do TDD são quase como um mantra que os
desenvolvedores seguem, conhecidos como:
	* Red;
	* Green;
	* Refactor.

"""


class Cat:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def meow(self):
        print(f"{self.__name} is meowing...")


# Teste manual:
cat_1 = Cat('Felix')
print(f"cat_1.name: {cat_1.name}")
cat_1.meow()

