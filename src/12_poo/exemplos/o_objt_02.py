# Criando uma classe
# Definição da classe Fuctura para representar informações sobre alunos
class Fuctura():
    def __init__(self, nome, matricula, telefone, email):
        # Inicialização dos atributos da instância com os valores fornecidos
        self.aluno = nome
        self.matricula = matricula
        self.telefone = telefone
        self.email = email

# Criando instâncias da classe Fuctura com diferentes conjuntos de informações
aluno1 = Fuctura("João Paulo II", "111", "99192-9394", "joaopaulo2@gmail.com")
# Impressão do nome do aluno1
print(aluno1.aluno)

aluno2 = Fuctura("Al Pacino", "101", "99999-8888", "alpacino@gmail.con")
print(aluno2.aluno)

aluno3 = Fuctura("Salvador Dali", "121", "98182-8384", "salvadordali@gmail.com")
print(aluno3.aluno)
