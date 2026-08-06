# Chamando os resultados da função acessando atributos diretamente
class Fuctura():
    def __init__(self):
        self.aluno = "Paul McCartney"
        self.matricula = "101"
        self.telefone = "99192-9394"
        self.email = "paulmccartney@gmail.com"

# Instanciando a classe
fuctura_objeto = Fuctura()

# Acessando os atributos diretamente
print("Aluno:", fuctura_objeto.aluno)
print("Matrícula:", fuctura_objeto.matricula)
print("Telefone:", fuctura_objeto.telefone)
print("Email:", fuctura_objeto.email) 