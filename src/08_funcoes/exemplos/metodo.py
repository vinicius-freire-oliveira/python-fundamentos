# Chamando os resultados da função acessando atributos por meio de métodos
# Definindo um método para acessar os atributos
class Fuctura():
    def __init__(self):
        self.aluno = "Paul McCartney"
        self.matricula = "101"
        self.telefone = "99192-9394"
        self.email = "paulmccartney@gmail.com"

def obter_detalhes(objeto):
    return (objeto.aluno, objeto.matricula, objeto.telefone, objeto.email)

# Instanciando a classe
fuctura_objeto = Fuctura()

# Chamando o método para obter os detalhes
aluno, matricula, telefone, email = obter_detalhes(fuctura_objeto)

# Imprimindo os detalhes
print("Aluno:", aluno)
print("Matrícula:", matricula)
print("Telefone:", telefone)
print("Email:", email)