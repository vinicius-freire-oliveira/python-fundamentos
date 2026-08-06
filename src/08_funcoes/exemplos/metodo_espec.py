# Chamando os resultados da função usando métodos específicos
class Fuctura:
    def __init__(self):
        self.aluno = "Paul McCartney"
        self.matricula = "101"
        self.telefone = "99192-9394"
        self.email = "paulmccartney@gmail.com"

    # Método para obter o aluno
    def obter_aluno(self):
        return self.aluno

    # Método para obter a matrícula
    def obter_matricula(self):
        return self.matricula

    # Método para obter o telefone
    def obter_telefone(self):
        return self.telefone
    
    # Método para obter o email
    def obter_email(self):
        return self.email

# Instanciando a classe
fuctura_objeto = Fuctura()

# Chamando os métodos para obter os atributos
print("Aluno:", fuctura_objeto.obter_aluno())
print("Matrícula:", fuctura_objeto.obter_matricula())
print("Telefone:", fuctura_objeto.obter_telefone())
print("Email:", fuctura_objeto.obter_email())