# Criando uma classe
# Definição da classe Fuctura para representar informações sobre alunos
class Fuctura():
    def __init__(self):
        # Inicialização dos atributos padrão da instância
        self.aluno = "Juscelino Kubitschek"
        self.matricula = "201"
        self.telefone = "98888-9999"
        self.email = "Juscelino_Kubitschek@gmail.com"

# Criação de uma instância da classe Fuctura
aluno1 = Fuctura()
# Impressão do nome do aluno1
print(aluno1.aluno)

aluno2 = Fuctura()
print(aluno2.aluno)

# Atribuição de um novo atributo 'status' para a instância aluno2
aluno2.status = 2
# Impressão do status da instância aluno2
print(aluno2.status)
