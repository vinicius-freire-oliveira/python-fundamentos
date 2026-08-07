# Define a classe Produto
class Produto:
    # Método construtor para inicializar os atributos codigo, preco e quantidade
    def __init__(self, codigo, preco, quantidade):
        # Atributo privado __codigo para armazenar o código do produto
        self.__codigo = codigo
        # Atributo privado __preco para armazenar o preço do produto
        self.__preco = preco
        # Atributo privado __quantidade para armazenar a quantidade do produto
        self.__quantidade = quantidade

    # Método getter para obter a quantidade do produto
    def get_quantidade(self):
        return self.__quantidade

    # Método setter para definir a quantidade do produto
    def set_quantidade(self, nova_quantidade):
        self.__quantidade = nova_quantidade

    # Método para adicionar uma quantidade especificada ao estoque do produto
    def adicionar(self, valor):
        # Obtém a quantidade atual do produto e adiciona o valor especificado
        self.set_quantidade(self.get_quantidade() + valor)

    # Método para remover uma quantidade especificada do estoque do produto
    def remover(self, valor):
        # Obtém a quantidade atual do produto e remove o valor especificado
        self.set_quantidade(self.get_quantidade() - valor)

# Cria uma instância da classe Produto com os parâmetros especificados
produto = Produto(1, 10.99, 5)

# Obtém e imprime a quantidade atual do produto
quantidade_atual = produto.get_quantidade()
print(quantidade_atual)  # Saída: 5

# Adiciona 3 unidades ao estoque do produto
produto.adicionar(3)

# Obtém e imprime a quantidade atualizada do produto após a adição
quantidade_atualizada = produto.get_quantidade()
print(quantidade_atualizada)  # Saída: 8

# Remove 2 unidades do estoque do produto
produto.remover(2)

# Obtém e imprime a quantidade atualizada do produto após a remoção
quantidade_atualizada = produto.get_quantidade()
print(quantidade_atualizada)  # Saída: 6

