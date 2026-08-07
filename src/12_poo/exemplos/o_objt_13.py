# Sobrecarga de Métodos
# Definição da classe Lar
class Lar():
    # Método toctoc que simula alguém batendo na porta
    def toctoc(self, pessoa1=None, pessoa2=None):
        # Verifica se pelo menos uma pessoa bateu na porta
        if pessoa1 is not None and pessoa2 is None:
            # Se apenas uma pessoa bateu na porta, imprime uma saudação com o nome dessa pessoa
            print("Olá, " + pessoa1)
        # Verifica se duas pessoas bateram na porta
        elif pessoa1 is not None and pessoa2 is not None:
            # Se duas pessoas bateram na porta, imprime uma saudação com os nomes dessas pessoas
            print("Olá, " + pessoa1 + " e " + pessoa2)
        else:
            # Se ninguém bateu na porta, imprime uma mensagem genérica
            print("Quem está aí?")

# Instanciação da classe Lar
batendoNaPorta = Lar()

# Chamada do método toctoc com dois nomes de pessoas
batendoNaPorta.toctoc("Ricky", "Morty")

# Chamada do método toctoc com um nome de pessoa
batendoNaPorta.toctoc("Professor Raimundo Nonato")