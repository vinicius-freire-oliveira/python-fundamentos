# A classe "ContaSalario" possui um construtor __init__, que recebe um parâmetro "codigo" e inicializa os atributos "_codigo" e "_saldo" com os valores passados e 0, respectivamente.
class ContaSalario:
  
  def __init__(self, codigo):
    self._codigo = codigo
    self._saldo = 0

# A classe também possui o método __eq__, que permite comparar duas instâncias da classe "ContaSalario" pelo atributo "_codigo" e "_saldo". Se os códigos e saldos forem iguais, o método retorna True, indicando que as duas contas são consideradas iguais.
  def __eq__(self, outro):
    return self._codigo == outro._codigo and self._saldo == outro._saldo
  
  def deposita(self, valor):
    self._saldo += valor
    
  def __str__(self):
    return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)

""" Nesta parte, são criadas duas instâncias da classe "ContaSalario": "conta1" com código 37 e "conta2" também com código 37. Em seguida, é feita uma comparação entre "conta1" e "conta2" usando o operador de igualdade (==). O resultado dessa comparação será True, pois as duas contas têm o mesmo código e saldo. """
conta1 = ContaSalario(37)
conta2 = ContaSalario(37)
print(conta1 == conta2)

# Aqui, é chamado o método "deposita" da instância "conta1" com o valor 10. Como resultado, o saldo da conta1 é atualizado para 10.
conta1.deposita(10)

""" Em seguida, é feita novamente a comparação entre "conta1" e "conta2" usando o operador ==. O resultado dessa comparação será False, pois o saldo de "conta1" é diferente do saldo de "conta2" (10 e 0, respectivamente). Portanto, após o depósito, as contas já não são mais consideradas iguais. """
print(conta1 == conta2)
