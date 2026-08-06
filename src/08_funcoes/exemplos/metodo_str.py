# Chamando os resultados da função usando o método __str__
class Fuctura:
    def __init__(self):
        self.aluno = "Paul McCartney"
        self.matricula = "101"
        self.telefone = "99192-9394"
        self.email = "paulmccartney@gmail.com"

    # Método especial para retornar uma representação em string do objeto
    def __str__(self):
        return f"Aluno: {self.aluno}\nMatrícula: {self.matricula}\nTelefone: {self.telefone}\nEmail: {self.email}"

# Instanciando a classe
fuctura_objeto = Fuctura()

# Chamando o método __str__
print(fuctura_objeto)