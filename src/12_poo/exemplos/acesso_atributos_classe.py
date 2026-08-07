""" class Livro:
    def __init__(self, titulo, autor, preco, estoque):
        self.titulo = titulo
        self.autor = autor
        self.preco = preco
        self.estoque = estoque

livro = Livro("I'm your man - A vida de Leonard Cohen", "Sylvie Simmons", 40.00, 100)

print(livro.preco)
print(livro.autor)
print(livro.estoque)
print(livro.titulo) """

# Definição da classe Livro
class Livro:
    # Método construtor para inicializar os atributos do livro
    def __init__(self, titulo, autor, preco, estoque):
        # Atribui o valor do parâmetro titulo ao atributo titulo da instância
        self.titulo = titulo
        # Atribui o valor do parâmetro autor ao atributo autor da instância
        self.autor = autor
        # Atribui o valor do parâmetro preco ao atributo preco da instância
        self.preco = preco
        # Atribui o valor do parâmetro estoque ao atributo estoque da instância
        self.estoque = estoque

# Cria uma nova instância da classe Livro com os valores fornecidos
livro = Livro("I'm your man - A vida de Leonard Cohen", "Sylvie Simmons", 40.00, 100)

# Imprime o valor do atributo preco da instância livro
print(livro.preco)
