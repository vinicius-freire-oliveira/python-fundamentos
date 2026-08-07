# Orientação a Objeto (__name__)
# Definição da classe Fuctura
class Fuctura():
    # Método construtor (__init__) que inicializa os atributos da classe
    def __init__(self, nome, matricula, telefone, email, funcionarios):
        # Inicialização dos atributos aluno, matricula, telefone, email e funcionarios
        self.aluno = nome
        self.matricula = matricula
        self.telefone = telefone
        self.email = email
        self.funcionarios = funcionarios
        # Atributo de verificação que armazena o nome da classe (Fuctura)
        self.verificação = self.__class__.__name__

    # Método para apresentar uma mensagem de boas-vindas
    def apresentação(self):
        # Imprime uma mensagem de boas-vindas com o nome da classe
        print(f"Bem vindo ao Fuctura! aluno da filial: {self.verificação}")

# Instanciando um objeto aluno1 da classe Fuctura com valores iniciais para os atributos
aluno1 = Fuctura("Albert Einstein", None, None, None, None)
# Imprime o valor do atributo aluno do objeto aluno1
print(aluno1.aluno)
# Chama o método apresentação() do objeto aluno1
aluno1.apresentação()

aluno2 = Fuctura("Thomas Edison", None, None, None, None)
print(aluno2.aluno)
aluno2.apresentação()