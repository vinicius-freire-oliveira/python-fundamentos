# Define a classe base Relatorio
class Relatorio:
    # Método que gera um relatório geral
    def gera_relatorio(self):
        print('Relatório geral')

# Define a classe RelatorioUsuarios que herda de Relatorio
class RelatorioUsuarios(Relatorio):
    # Sobrescreve o método gera_relatorio para gerar um relatório de usuários
    def gera_relatorio(self):
        print('Relatório dos usuários')

# Define a classe RelatorioCustos que herda de Relatorio
class RelatorioCustos(Relatorio):
    # Sobrescreve o método gera_relatorio para gerar um relatório de custos
    def gera_relatorio(self):
        print('Relatório de custos')

# Cria uma instância da classe RelatorioUsuarios
relatorio1 = RelatorioUsuarios()
# Cria uma instância da classe RelatorioCustos
relatorio2 = RelatorioCustos()
# Cria outra instância da classe RelatorioUsuarios
relatorio3 = RelatorioUsuarios()
# Cria mais uma instância da classe RelatorioUsuarios
relatorio4 = RelatorioUsuarios()

# Cria uma lista de relatórios contendo as instâncias criadas
relatorios = [relatorio1, relatorio2, relatorio3, relatorio4]

# Itera sobre a lista de relatórios
for rel in relatorios:
    # Chama o método gera_relatorio para cada instância
    rel.gera_relatorio()
