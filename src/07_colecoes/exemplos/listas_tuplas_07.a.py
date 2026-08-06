# Verifica se 15 é menor que 32 e imprime o resultado (True)
print(15 < 32)

""" 
Aqui, é criada uma lista chamada "nomes" contendo strings. A função "sorted()" é usada para ordenar essa lista em ordem alfabética e, em seguida, é impressa a lista ordenada. 
Repare que a ordem é feita primeiramente com aqueles elementos em maiúsculo e depois o minúsculo.
"""
nomes = ["guilherme", "Daniela", "Paulo"]
print(sorted(nomes))

""" 
Nesta parte, é definida a classe ContaSalario com atributos e métodos. Em seguida, três instâncias da classe ContaSalario são criadas e algumas operações são realizadas sobre elas. 
Após isso, as contas são adicionadas à lista "contas" e, em seguida, cada conta é impressa usando um loop for.
"""
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

# Criação de instâncias da classe ContaSalario e operações de depósito
conta_do_guilherme = ContaSalario(17)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(510)

# Lista que contém as instâncias de ContaSalario criadas anteriormente
contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

# Imprime cada conta usando um loop for
for conta in contas:
  print(conta)

#sorted(contas)

#conta_do_guilherme < conta_da_daniela

""" 
É definida a função extrai_saldo(conta) que retorna o saldo de uma conta. 
Em seguida, um loop for é utilizado para imprimir as contas da lista "contas" ordenadas com base no saldo, 
utilizando a função sorted() com a chave de ordenação "extrai_saldo". 
Essa parte do código ordena a lista de contas com base no saldo de cada conta e, em seguida, imprime as contas em ordem crescente com base no saldo. 
O resultado será uma lista de contas ordenadas do menor saldo para o maior saldo.
"""
def extrai_saldo(conta):
  return conta._saldo

# Ordena e imprime as contas com base no saldo utilizando a função sorted() e a chave extrai_saldo
for conta in sorted(contas, key=extrai_saldo):
  print(conta)

""" 
É importado o módulo attrgetter da biblioteca operator. 
Através do loop for, as contas da lista "contas" são impressas novamente, mas desta vez são ordenadas com base no atributo _saldo, 
usando attrgetter("_saldo") como a chave de ordenação para a função sorted(). 
Ambas as abordagens (extrai_saldo e attrgetter("_saldo")) alcançam o mesmo resultado, ordenando a lista de contas com base no saldo.
"""
from operator import attrgetter

""" 
O key=attrgetter("_saldo") especifica que queremos usar o atributo _saldo como chave de ordenação. 
O uso do attrgetter torna o código mais conciso e legível para acessar atributos específicos ao ordenar objetos.
"""
for conta in sorted(contas, key=attrgetter("_saldo")):
  print(conta)
