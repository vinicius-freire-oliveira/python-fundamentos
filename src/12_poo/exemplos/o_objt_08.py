# Orientação a Objeto

# Definição da classe Fuctura para representar informações sobre alunos e funcionários
class Fuctura():
    def __init__(self, nome, matricula, telefone, email, funcionarios):
        # Inicialização dos atributos da instância com os valores fornecidos
        self.aluno = nome
        self.matricula = matricula
        self.telefone = telefone
        self.email = email
        self.funcionarios = funcionarios
    
    # Método para realizar uma apresentação da instituição
    def apresentação(self):
        print("Bem-vindo a Fuctura")

# Criação de uma instância da classe Fuctura com informações de um aluno e funcionários
aluno1 = Fuctura("Roberto Carlos", 121, 31323334, "rb@gmail.com", 30)
# Impressão do nome do aluno1
print(aluno1.aluno)
# Chama o método apresentação() para realizar uma apresentação da instituição
aluno1.apresentação()

aluno2 = Fuctura("Jô Soares", None, None, None, None)
print(aluno2.aluno)
aluno2.apresentação()
