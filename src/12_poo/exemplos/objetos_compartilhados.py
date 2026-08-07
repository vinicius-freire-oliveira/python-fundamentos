# Define a classe Funcionario
class Funcionario:
    # Método construtor para inicializar os atributos nome e salario
    def __init__(self, nome, salario):
        # Atributo público nome para armazenar o nome do funcionário
        self.nome = nome
        # Atributo público salario para armazenar o salário do funcionário
        self.salario = salario

# Cria uma instância da classe Funcionario com o nome "Ana" e um salário de 5000, atribuindo-a à variável 'ana'
ana = Funcionario("Ana", 5000)

# Cria uma nova referência 'joaquim' que aponta para o mesmo objeto que 'ana'
joaquim = ana

# Modifica o salário do funcionário referenciado por 'joaquim'
joaquim.salario = 2500

# Imprime o salário do funcionário referenciado por 'joaquim'
print("Salário de Joaquim: ", joaquim.salario)

# Imprime o salário do funcionário referenciado por 'ana'
print("Salário de Ana: ", ana.salario)
