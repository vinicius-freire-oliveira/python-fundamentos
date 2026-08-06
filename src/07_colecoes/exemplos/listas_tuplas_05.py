""" A classe "Conta" representa uma conta genérica, com código e saldo. Ela possui um construtor __init__ que recebe um parâmetro "codigo" e inicializa os atributos "_codigo" e "_saldo" com os valores passados e 0, respectivamente. """
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

""" Neste trecho, é criada uma instância da classe "Conta" com código 88 e, em seguida, o método __str__ é chamado para imprimir uma representação em string da conta, mostrando o código e o saldo. """
print(Conta(88))

# A classe "ContaCorrente" também representa uma conta. A classe possui o método "deposita" para incrementar o saldo da conta. 
class ContaCorrente:
  
  def __init__(self, codigo):
    self.codigo = codigo
    self.saldo = 0

  def deposita(self, valor):
    self.saldo += valor
    
  def __str__(self):
    return "[>>Codigo {} Saldo {}<<]".format(self.codigo, self.saldo)

""" Neste bloco, são criadas instâncias das classes "ContaCorrente" com diferentes códigos, e são realizados depósitos nas contas. Em seguida, as informações das contas são impressas usando o método __str__. """
conta_do_gui = ContaCorrente(15)
print(conta_do_gui)

conta_do_gui.deposita(500)
print(conta_do_gui)

conta_da_dani = ContaCorrente(47685)
conta_da_dani.deposita(1000)
print(conta_da_dani)

contas = [conta_do_gui, conta_da_dani]
for conta in contas:
  print(conta)

""" A classe "ContaSalario" representa outra conta, com atributos "_codigo" e "_saldo" que são inicializados no construtor. Além disso, a classe possui um método __eq__, que permite comparar duas instâncias da classe "ContaSalario" verificando se os códigos e saldos são iguais. """
class ContaSalario:
  
  def __init__(self, codigo):
    self._codigo = codigo
    self._saldo = 0
    
  def __eq__(self, outro):
    if type(outro) != ContaSalario:
      return False
    
    return self._codigo == outro._codigo and self._saldo == outro._saldo
  
  def deposita(self, valor):
    self._saldo += valor
    
  def __str__(self):
    return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)

""" Aqui são criadas duas instâncias, uma da classe "ContaSalario" (conta1) e outra da classe "ContaCorrente" (conta2). Em seguida, é feita uma comparação com o operador de igualdade (==) entre as duas contas. Como as classes são diferentes, o método __eq__ da classe "ContaSalario" não é chamado, e a comparação retorna False. """
conta1 = ContaSalario(37)
conta2 = ContaCorrente(37)

print(conta1 == conta2)

""" Nesta parte, é utilizada a função isinstance() para verificar se uma instância da classe "ContaCorrente" é uma instância de "ContaCorrente" e de "Conta". A primeira verificação retorna True, pois a instância é realmente da classe "ContaCorrente". A segunda verificação retorna False, pois a instância é da classe "ContaCorrente" e não da classe "Conta". """
print(isinstance(ContaCorrente(34), ContaCorrente))

print(isinstance(ContaCorrente(34), Conta))

# Nesse bloco, é criada uma lista de idades e são feitas iterações sobre ela utilizando range, enumerate, e desempacotamento de tuplas para obter os índices e idades.
idades = [15, 87, 32, 65, 56, 32, 49, 37]

for i in range(len(idades)):
  print(i, idades[i])

print(range(len(idades))) # lazy...

print(enumerate(idades)) # lazy

print(list(range(len(idades)))) # forcei a geração dos valores

print(list(enumerate(idades)))

for indice, idade in enumerate(idades): # unpacking da nossa tupla
  print(indice, "x", idade)

""" Neste trecho, temos uma lista de tuplas chamada "usuarios", contendo informações de nomes, idades e anos de nascimento. Em seguida, são feitas iterações para imprimir apenas os nomes e ignorar o resto das informações das tuplas. """
usuarios = [
    ("Guilherme", 37, 1981),
    ("Daniela", 31, 1987),
    ("Paulo", 39, 1979)
]

for nome, idade, nascimento in usuarios: # ja desempacotando
  print(nome)

for nome, _, _ in usuarios: # ja desempacotando, ignorando o resto
  print(nome)