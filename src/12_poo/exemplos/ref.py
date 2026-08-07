# Define a classe Colaborador
class Colaborador:
    # Método construtor para inicializar os atributos nome e salario
    def __init__(self, nome, salario):
        # Atributo público nome para armazenar o nome do colaborador
        self.nome = nome
        # Atributo público salario para armazenar o salário do colaborador
        self.salario = salario

# Cria uma instância da classe Colaborador com os parâmetros especificados
bernardo = Colaborador("Bernardo", 5000)

# Cria uma nova referência 'outraRef' para o mesmo objeto 'bernardo'
outraRef = bernardo

# Imprime o nome e o salário do colaborador 'bernardo'
print("Nome: ", bernardo.nome)
print("Salário: ", bernardo.salario)

# Imprime o nome e o salário do colaborador referenciado por 'outraRef'
print("Nome: ", outraRef.nome)
print("Salário: ", outraRef.salario)
