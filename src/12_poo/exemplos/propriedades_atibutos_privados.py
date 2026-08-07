# Define a classe Pessoa
class Pessoa:
    # Método construtor para inicializar os atributos nome e idade
    def __init__(self, nome, idade):
        # Atributo privado __nome para armazenar o nome da pessoa
        self.__nome = nome
        # Atributo privado __idade para armazenar a idade da pessoa
        self.__idade = idade

    # Método getter para obter o nome da pessoa
    @property
    def nome(self):
        return self.__nome

    # Método setter para definir o nome da pessoa
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

# Cria uma instância da classe Pessoa com o nome "Nelsinho Batista" e idade 75
pessoa = Pessoa("Nelsinho Batista", 75)

# Obtém e imprime o nome da pessoa usando o método getter @property
print(pessoa.nome)  # Saída: Nelsinho Batista

