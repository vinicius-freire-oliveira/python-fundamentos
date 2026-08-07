# Criando uma classe
# Define a classe Fuctura
class Fuctura():
    # Método de inicialização da classe
    def __init__(self):
        # Define e inicializa os atributos com os valorres
        self.aluno = "Paul McCartney"
        self.matricula = "101"
        self.telefone = "99192-9394"
        self.email = "paulmccartney@gmail.com"

# Cria uma instância da classe Fuctura e atribui à variável aluno1
aluno1 = Fuctura()
# Imprime o valor do atributo aluno da instância aluno1
print(aluno1.aluno)

aluno2 = Fuctura()
print(aluno2.aluno)

aluno3 = Fuctura()
print(aluno3.aluno)
