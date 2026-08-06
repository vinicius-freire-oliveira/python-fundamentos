#conta_do_guilherme < conta_da_daniela

# Definindo a classe ContaSalario
class ContaSalario:

  # Método de inicialização da classe, recebe o código como parâmetro e inicia o saldo em 0
  def __init__(self, codigo):
    self._codigo = codigo
    self._saldo = 0
    
  # Método de igualdade que compara duas instâncias de ContaSalario para verificar se são iguais
  def __eq__(self, outro):
    if type(outro) != ContaSalario:
      return False
    
    return self._codigo == outro._codigo and self._saldo == outro._saldo
  
  # Método de comparação "menor que" entre duas instâncias de ContaSalario
  def __lt__(self, outro):
    return self._saldo < outro._saldo
  
  # Método para realizar um depósito na conta, aumentando o saldo
  def deposita(self, valor):
    self._saldo += valor
    
  # Método que retorna uma representação em string da conta, mostrando o código e o saldo
  def __str__(self):
    return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)

# Criando instâncias da classe ContaSalario
conta_do_guilherme = ContaSalario(17)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(510)

# Criando uma lista com as contas criadas
contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

# Comparando se a conta_do_guilherme é menor que a conta_da_daniela
print(conta_do_guilherme < conta_da_daniela)

# Comparando se a conta_do_guilherme é maior que a conta_da_daniela
print(conta_do_guilherme > conta_da_daniela)

# Iterando sobre a lista de contas, ordenadas por padrão usando o método __lt__
for conta in sorted(contas):
  print(conta)

# Iterando sobre a lista de contas, ordenadas em ordem reversa usando o método __lt__
for conta in sorted(contas,reverse=True):
  print(conta)
