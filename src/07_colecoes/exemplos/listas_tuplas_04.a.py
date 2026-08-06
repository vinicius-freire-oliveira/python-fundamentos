""" Nesta parte, é definida a classe "ContaSalario". Essa classe possui um construtor __init__, que recebe um parâmetro "codigo" e inicializa os atributos "_codigo" e "_saldo" com os valores passados e 0, respectivamente.  """
class ContaSalario:
  
  def __init__(self, codigo):
    self._codigo = codigo
    self._saldo = 0

 # A classe também possui o método "deposita" que permite depositar um valor na conta salário, incrementando o saldo da mesma com esse valor.  
  def deposita(self, valor):
    self._saldo += valor

 # O método __str__ retorna uma representação em string da conta salário, mostrando o código e o saldo.   
  def __str__(self):
    return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)

""" Nesta parte, são criadas duas instâncias da classe "ContaSalario": "conta1" com código 37 e "conta2" também com código 37. Em seguida, os valores dessas contas são impressos na tela usando o método __str__. """
conta1 = ContaSalario(37)
print(conta1)

conta2 = ContaSalario(37)
print(conta2)

""" É feita uma comparação entre "conta1" e "conta2" usando o operador de igualdade (==). O resultado dessa comparação será False, porque as duas contas são diferentes objetos, apesar de terem o mesmo código. """
print(conta1 == conta2)

""" Neste trecho, é criada uma lista chamada "contas" que contém apenas a conta "conta1". Em seguida, é verificado se "conta1" e "conta2" estão na lista "contas" usando o operador in. O resultado será True para "conta1 in contas", pois "conta1" está na lista, mas será False para "conta2 in contas", pois "conta2" não está na lista. Isso acontece porque "conta1" e "conta2" são objetos diferentes, mesmo que tenham o mesmo código. """
contas = [conta1]
print(conta1 in contas)

print(conta2 in contas)