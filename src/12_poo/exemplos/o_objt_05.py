# Criando uma classe
# Definição da classe Fuctura para representar informações sobre alunos
class Fuctura():
    def __init__(self, nome, matricula, telefone, email):
        # Inicialização dos atributos da instância com os valores fornecidos
        self.aluno = nome
        self.matricula = matricula
        self.telefone = telefone
        self.email = email
    
    def apresentacao(self):
        # Método para imprimir uma mensagem de boas-vindas ao aluno
        print("Bem-vindo(a) à Fuctura, {}!\n".format(self.aluno))

# Solicita ao usuário para inserir informações sobre o primeiro aluno
nome = input("Digite o nome do aluno: ")
matricula = input("Digite a matrícula do aluno: ")
telefone = input("Digite o telefone do aluno: ")
email = input("Digite o email do aluno: ")

# Cria uma instância da classe Fuctura com as informações fornecidas pelo usuário
aluno1 = Fuctura(nome, matricula, telefone, email)
# Chama o método apresentacao() para imprimir uma mensagem de boas-vindas ao aluno1
aluno1.apresentacao()

# Solicita ao usuário para inserir informações sobre o segundo aluno
nome = input("Digite o nome do aluno: ")
matricula = input("Digite a matrícula do aluno: ")
telefone = input("Digite o telefone do aluno: ")
email = input("Digite o email do aluno: ")

aluno2 = Fuctura(nome, matricula, telefone, email)
aluno2.apresentacao()
