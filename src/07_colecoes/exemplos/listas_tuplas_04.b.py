# A classe "ContaSalario" possui o construtor __init__, que recebe um parâmetro "codigo" e inicializa os atributos "_codigo" e "_saldo" com os valores passados e 0, respectivamente. 
class ContaSalario:
  
  def __init__(self, codigo):
    self._codigo = codigo
    self._saldo = 0

# A classe possui o método __eq__, que foi sobrescrito. Esse método permite comparar duas instâncias da classe "ContaSalario" pelo atributo "_codigo". Se os códigos forem iguais, o método retorna True, indicando que as duas contas são consideradas iguais.
  def __eq__(self, outro):
    return self._codigo == outro._codigo
  
  def deposita(self, valor):
    self._saldo += valor
    
  def __str__(self):
    return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)

# Nesta parte, são criadas duas instâncias da classe "ContaSalario": "conta1" com código 37 e "conta2" também com código 37.
conta1 = ContaSalario(37)
conta2 = ContaSalario(37)

# É feita uma comparação entre "conta1" e "conta2" usando o operador de igualdade (==). O resultado dessa comparação será True, pois as duas contas têm o mesmo código (37).
print(conta1 == conta2)

# Neste caso, é feita a comparação usando o operador de desigualdade (!=). O resultado será False, pois as duas contas têm o mesmo código e, portanto, não são consideradas diferentes.
print(conta1 != conta2)

# Aqui, é verificado se "conta1" está na lista que contém "conta2" usando o operador in. O resultado será True, pois "conta1" está presente na lista.
print(conta1 in [conta2])

# Neste caso, é verificado se "conta2" está na lista que contém "conta1". O resultado também será True, pois "conta2" está na lista.
print(conta2 in [conta1])