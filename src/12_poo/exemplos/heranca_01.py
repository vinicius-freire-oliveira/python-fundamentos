"""# Herança e polimorfismo"""

""" Definida uma classe chamada "Conta". A classe tem um construtor __init__, que recebe um parâmetro "codigo" e inicializa os atributos privados "_codigo" e "_saldo". Os atributos "_codigo" e "_saldo" são marcados como privados utilizando um underscore antes de seus nomes (convenção de nomenclatura em Python)."""
class Conta:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

# Classe possui um método chamado "deposita" que recebe um valor como parâmetro e incrementa o saldo da conta com esse valor.
    def deposita(self, valor):
        self._saldo += valor

# A classe sobrescreve o método __str__, que retorna uma representação em string da conta, mostrando o código e o saldo da conta.
    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)

# A classe é testada criando uma instância de "Conta" com código 88 e imprimindo-a.

print(Conta(88))

""" Neste trecho, temos uma definição de classe que utiliza o módulo "abc" (Abstract Base Classes) para criar uma classe abstrata. """
""" Nesta linha, são importados do módulo "abc" as classes "ABCMeta" e "abstractmethod". A classe "ABCMeta" é usada para criar classes abstratas, enquanto o decorador "abstractmethod" é usado para definir um método abstrato dentro da classe. """
from abc import ABCMeta, abstractmethod

# Aqui é definida a classe "Conta" como uma classe abstrata. Isso é indicado pela presença do argumento "metaclass=ABCMeta" na definição da classe.
class Conta(metaclass=ABCMeta):

# Este é o construtor da classe "Conta". Ele recebe um parâmetro "codigo" e inicializa os atributos "_codigo" e "_saldo" com os valores passados e 0, respectivamente.
  def __init__(self, codigo):
    self._codigo = codigo
    self._saldo = 0

# Este é um método da classe "Conta" que permite depositar um valor na conta. O valor é adicionado ao atributo "_saldo".
  def deposita(self, valor):
    self._saldo += valor

# Este é um método abstrato da classe "Conta". Métodos abstratos são definidos sem implementação (apenas o "pass" é utilizado) e devem ser implementados nas subclasses concretas. Neste caso, o método "passa_o_mes" é declarado como abstrato, o que significa que todas as subclasses concretas de "Conta" devem implementar esse método.
  @abstractmethod
  def passa_o_mes(self):
    pass
  
#Este é um método para representação em string da conta. Quando a classe "Conta" ou suas subclasses são convertidas para uma string, este método é chamado para retornar uma representação formatada da conta, mostrando o código e o saldo.
    def __str__(self):
       return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)

""" Nesta linha, é criada uma instância da classe abstrata "Conta" com código 88. No entanto, uma classe abstrata não pode ser instanciada diretamente. Se esse código for executado, um TypeError será gerado informando que não é possível instanciar a classe abstrata. O objetivo dessa classe é servir como uma classe base para outras classes que representem tipos específicos de contas (por exemplo, "ContaCorrente" ou "ContaPoupanca"). Essas subclasses concretas devem herdar da classe abstrata "Conta" e implementar o método "passa_o_mes", que é obrigatório devido à declaração como método abstrato. """
# print(Conta(88))
