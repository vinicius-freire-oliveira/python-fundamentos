# Criando uma classe
# Definição da classe Fuctura para representar informações sobre alunos
class Fuctura():
    def __init__(self, nome, matricula, telefone, email):
        # Inicialização dos atributos da instância com os valores fornecidos
        self.aluno = nome
        self.matricula = matricula
        self.telefone = telefone
        self.email = email

# Solicita ao usuário para inserir informações sobre um aluno
nome = input("Digite o nome do aluno: ")
matricula = input("Digite a matrícula do aluno: ")
telefone = input("Digite o telefone do aluno: ")
email = input("Digite o email do aluno: ")

# Cria uma instância da classe Fuctura com as informações fornecidas pelo usuário
aluno1 = Fuctura(nome, matricula, telefone, email)
# Imprime as informações do aluno1
print(aluno1.aluno, aluno1.matricula, aluno1.telefone, aluno1.email)
