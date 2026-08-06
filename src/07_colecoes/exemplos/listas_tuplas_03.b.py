"""Essa é a classe base, que representa uma conta genérica. Ela possui um construtor __init__ que recebe um parâmetro "codigo" e inicializa os atributos privados "_codigo" e "_saldo"."""
class Conta:
  
  def __init__(self, codigo):
    self._codigo = codigo
    self._saldo = 0

# Classe possui um método "deposita" que recebe um valor como parâmetro e incrementa o saldo da conta com esse valor. 
  def deposita(self, valor):
    self._saldo += valor

# Sobrescreve o método __str__, que retorna uma representação em string da conta, mostrando o código e o saldo.
  def __str__(self):
    return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)

print(Conta(88))

""" Essa é uma classe que herda da classe "Conta". Isso é indicado pela expressão (Conta) na definição da classe. A classe "ContaCorrente" adiciona um novo método chamado "passa_o_mes", que é específico para contas correntes. Esse método é usado para deduzir uma taxa fixa mensal do saldo da conta corrente (nesse caso, 2 unidades monetárias). """
class ContaCorrente(Conta):
  
  def passa_o_mes(self):
    self._saldo -= 2

""" classe que herda da classe "Conta". Ela também possui o método "passa_o_mes", mas com uma lógica diferente da "ContaCorrente". Para contas poupança, o método "passa_o_mes" aumenta o saldo em 1% (1.01) e, em seguida, deduz uma taxa fixa (3 unidades monetárias). """
class ContaPoupanca(Conta):
  
  def passa_o_mes(self):
    self._saldo *= 1.01
    self._saldo -= 3

# instâncias são criadas e suas operações são realizadas
""" Aqui é criada uma instância da classe "ContaCorrente" chamada "conta16" com código 16. É feito um depósito de 1000 e o método "passa_o_mes" é chamado para deduzir a taxa mensal de 2 unidades monetárias do saldo da conta. """ 
conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta16.passa_o_mes()
print(conta16)

""" Aqui é criada uma instância da classe "ContaPoupanca" chamada "conta17" com código 17. É feito um depósito de 1000 e o método "passa_o_mes" é chamado para aumentar o saldo em 1% (1000 * 1.01 = 1010) e, em seguida, deduzir a taxa mensal de 3 unidades monetárias do saldo da conta. O estado da conta é impresso. """
conta17 = ContaPoupanca(17)
conta17.deposita(1000)
conta17.passa_o_mes()
print(conta17)

""" Aqui são criadas novas instâncias "conta16" e "conta17", e em seguida, são adicionadas a uma lista "contas". """
conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta17 = ContaPoupanca(17)
conta17.deposita(1000)
contas = [conta16, conta17]

""" Um loop "for" é utilizado para percorrer as contas na lista e chamar o método "passa_o_mes" para cada uma delas. """
for conta in contas:
  conta.passa_o_mes() # duck typing
  print(conta)

""" O polimorfismo de "duck typing" permite que o método seja chamado em cada conta, mesmo que as contas sejam de tipos diferentes (ContaCorrente e ContaPoupanca). O método correto será escolhido dinamicamente com base no tipo do objeto em tempo de execução. O estado das contas é impresso após cada passo do loop. """