# Definição da classe Receita
class Receita:

    # Método construtor para inicializar os atributos autor e tempo_preparo
    def __init__(self, autor, tempo_preparo):
        # Atributos privados __autor e __tempo_preparo
        self.__autor = autor
        self.__tempo_preparo = tempo_preparo

    # Getter para o atributo privado __autor
    @property
    def autor(self):
        return self.__autor

    # Setter para o atributo privado __autor
    @autor.setter
    def autor(self, autor):
        self.__autor = autor

    # Getter para o atributo privado __tempo_preparo
    @property
    def tempo_preparo(self):
        return self.__tempo_preparo

    # Setter para o atributo privado __tempo_preparo
    @tempo_preparo.setter
    def tempo_preparo(self, tempo_preparo):
        self.__tempo_preparo = tempo_preparo

# Cria uma instância da classe Receita com autor "João" e tempo_preparo 60
receita = Receita("Emerson Fittipaldi", 60)

# Imprime o valor do atributo autor da instância receita
print(receita.autor)  # Saída: João

# Imprime o valor do atributo tempo_preparo da instância receita
print(receita.tempo_preparo)  # Saída: 60

# Define um novo valor para o atributo autor da instância receita
receita.autor = "Michael Jordan"

# Define um novo valor para o atributo tempo_preparo da instância receita
receita.tempo_preparo = 45

# Imprime o novo valor do atributo autor da instância receita
print(receita.autor)  # Saída: Maria

# Imprime o novo valor do atributo tempo_preparo da instância receita
print(receita.tempo_preparo)  # Saída: 45

