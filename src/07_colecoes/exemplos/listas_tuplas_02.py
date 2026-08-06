"""# Objetos próprios"""

# Neste trecho, é definida uma classe chamada "ContaCorrente", que possui um construtor __init__ responsável por inicializar os atributos "codigo" e "saldo".
class ContaCorrente:
  
  def __init__(self, codigo):
    self.codigo = codigo
    self.saldo = 0

# A classe também possui um método "deposita" que incrementa o saldo da conta com o valor passado como parâmetro.
  def deposita(self, valor):
    self.saldo += valor

# O método __str__ é sobrescrito para definir como a representação em string do objeto será exibida.
  def __str__(self):
    return "[>>Codigo {} Saldo {}<<]".format(self.codigo, self.saldo)

# Neste trecho, é criada instância da classe "ContaCorrente": "conta_do_gui" com código 15.
conta_do_gui = ContaCorrente(15)
print(conta_do_gui)

conta_do_gui.deposita(500)
# seus dados são impressos usando o método __str__. 
print(conta_do_gui)

# Neste trecho, é criada instância da classe "ContaCorrente": conta_da_dani" com código 47685.
conta_da_dani = ContaCorrente(47685)
conta_da_dani.deposita(1000)
# seus dados são impressos usando o método __str__.
print(conta_da_dani)

"""Neste trecho, é criada uma lista "contas" que contém as instâncias "conta_do_gui" e "conta_da_dani". Um loop "for" é utilizado para imprimir as informações de cada conta usando o método __str__."""
contas = [conta_do_gui, conta_da_dani]
for conta in contas:
  print(conta)

contas = [conta_do_gui, conta_da_dani, conta_do_gui]

print(contas[0])

conta_do_gui.deposita(100)

print(contas[0])

print(conta_do_gui)

print(contas[2])

contas[2].deposita(300)

print(conta_do_gui)

"""Neste trecho, é definida a função "deposita_para_todas" que recebe uma lista de contas e deposita um valor fixo (100) em cada uma delas. A função é aplicada à lista "contas", demonstrando que a função age diretamente nas instâncias de "ContaCorrente" contidas na lista."""
def deposita_para_todas(contas):
  for conta in contas:
    conta.deposita(100)

contas = [conta_do_gui, conta_da_dani]
print(contas[0], contas[1])
deposita_para_todas(contas)
print(contas[0], contas[1])

contas.insert(0,76)
print(contas[0], contas[1], contas[2])

#deposita_para_todas(contas)
print(contas[0], contas[1], contas[2])

guilherme = ('Guilherme', 37, 1981) # tupla
daniela = ('Daniela', 31, 1987)
# paulo = (39, 'Paulo', 1979) # ruim

#guilherme.append(6754) # Resultará em um erro, pois tuplas são imutáveis.


conta_do_gui = (15, 1000)
# conta_do_gui.deposita() # Variação OO # tuplas não possuem métodos
print(conta_do_gui[1])

#conta_do_gui[1] += 100 # é tentado alterar o saldo da conta, mas isso resultará em um erro, pois tuplas são imutáveis.

"""Neste trecho, é definida a função "deposita" que recebe uma tupla representando uma conta e retorna uma nova tupla com o saldo atualizado. A função é aplicada à tupla "conta_do_gui", gerando uma nova tupla "conta_do_gui" com saldo atualizado. Em seguida, são criadas listas contendo informações de usuários"""
def deposita(conta): # variação "funcional"(separando o comportamento dos dados)
  novo_saldo = conta[1] + 100
  codigo = conta[0]
  return (codigo, novo_saldo)

print(deposita(conta_do_gui))

print(conta_do_gui)

conta_do_gui = deposita(conta_do_gui)
print(conta_do_gui)

usuarios = [guilherme, daniela]
print(usuarios)

usuarios.append(('Paulo', 39, 1979))

print(usuarios)

#usuarios[0][0] = 'Guilherme Silveira' # tentativa de alterar o nome do usuário "guilherme" é realizada, mas isso resultará em um erro, pois tuplas são imutáveis.

"""Neste trecho, são criadas duas instâncias da classe "ContaCorrente": "conta_do_gui" e "conta_da_dani". Em seguida, é criada uma tupla "contas" contendo essas duas instâncias."""
conta_do_gui = ContaCorrente(15)
conta_do_gui.deposita(500)
conta_da_dani = ContaCorrente(234876)
conta_da_dani.deposita(1000)

contas = (conta_do_gui, conta_da_dani)

# Um loop "for" é utilizado para imprimir as informações de cada conta usando o método __str__.
for conta in contas:
  print(conta)

#contas.append(423768) # Ao tentar adicionar um elemento à tupla "contas" ou depositar em uma das contas na tupla, isso resultará em um erro, pois tuplas são imutáveis.

contas[0].deposita(300)

for conta in contas:
  print(conta)