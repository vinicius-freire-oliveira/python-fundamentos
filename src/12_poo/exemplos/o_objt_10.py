# Comentário explicando a finalidade do código
# Orientação a Objeto

# Definição da classe Pessoa para representar informações sobre pessoas
class Pessoa():
    def __init__(self, nome, idade):
        # Inicialização dos atributos da instância com os valores fornecidos
        self.nome = nome
        self.idade = idade

# Criação de uma instância da classe Pessoa com nome "Bruce Lee" e idade 45
pessoa = Pessoa("Bruce Lee", 45)
# Impressão do nome e idade da pessoa
print(pessoa.nome)
print(pessoa.idade)
