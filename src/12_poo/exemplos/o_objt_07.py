# Criando uma classe
# Definição da classe Pessoa para representar pessoas
class Pessoa():
    def __init__(self, nome, idade):
        # Inicialização dos atributos da instância com os valores fornecidos
        self.nome = nome
        self.idade = idade

    # Método para imprimir as informações da pessoa
    def imprimir(self):
        print("Meu nome é %s tenho %d anos" %(self.nome, self.idade))

# Criação de uma instância da classe Pessoa com nome "Mandela" e idade 90
pessoa = Pessoa("Mandela", 90)
# Chama o método imprimir() para imprimir as informações da pessoa
pessoa.imprimir()
