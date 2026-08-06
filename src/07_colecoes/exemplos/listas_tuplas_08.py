# Definição da classe ContaSalario
class ContaSalario:
# O construtor da classe que recebe o código da conta como parâmetro e inicializa o saldo como zero.
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

# O método de comparação que verifica se duas contas são iguais. Para isso, verifica se o outro objeto é uma instância de ContaSalario e se os códigos e saldos são iguais.
    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        return self._codigo == outro._codigo and self._saldo == outro._saldo

# O método de comparação que verifica se uma conta é menor que outra, baseado no saldo. Ele é usado para ordenar as contas com base no saldo.
    def __lt__(self, outro):
        return self._saldo < outro._saldo

# Um método que recebe um valor como parâmetro e adiciona esse valor ao saldo da conta.
    def deposita(self, valor):
        self._saldo += valor

# O método que retorna uma representação em string da conta, mostrando o código e o saldo.
    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)

# Utilização da primeira definição da classe ContaSalario
""" Criamos três contas diferentes: conta_do_guilherme, conta_da_daniela e conta_do_paulo. Para cada conta, utilizamos o método deposita para adicionar valores aos saldos. Em seguida, colocamos essas contas em uma lista chamada contas.  """
conta_do_guilherme = ContaSalario(1700)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(500)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

# Utilizamos o for para percorrer essa lista ordenada (devido ao método sorted) e imprimir as contas com base no saldo. 
for conta in sorted(contas):
    print(conta)

# Comparamos o saldo de duas contas usando o operador <.
print(conta_do_guilherme < conta_da_daniela)

#conta_do_guilherme <= conta_da_daniela

# Segunda definição da classe ContaSalario usando @total_ordering
""" Utilizamos o decorador @total_ordering, que gera automaticamente os métodos de comparação faltantes (__ne__, __gt__, __ge__) com base nos métodos __eq__ e __lt__ que foram definidos. Essa definição permite que possamos usar os operadores de comparação (<=, >, >=, etc.) sem a necessidade de implementar todos os métodos manualmente. """
from functools import total_ordering

@total_ordering
class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        return self._codigo == outro._codigo and self._saldo == outro._saldo

    def __lt__(self, outro):
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo
        return self._codigo < outro._codigo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)

# Utilização da segunda definição da classe ContaSalario
""" Neste bloco, realizamos as mesmas operações que no primeiro, porém agora com a segunda definição da classe ContaSalario. Imprimimos os resultados de algumas comparações usando os operadores <=, <, ==, entre outros. """
conta_do_guilherme = ContaSalario(1700)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(500)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

print(conta_do_guilherme <= conta_da_daniela)
print(conta_do_guilherme <= conta_do_paulo)
print(conta_do_guilherme < conta_do_guilherme)
print(conta_do_guilherme == conta_do_guilherme)
print(conta_do_guilherme <= conta_do_guilherme)


