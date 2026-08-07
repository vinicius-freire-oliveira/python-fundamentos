# Sobrecarga de Métodos
# Definição da classe Lar
class Lar():
    # Método toctoc que simula alguém batendo na porta
    def toctoc(self, *pessoa):
        # Verifica se pelo menos uma pessoa foi fornecida
        if pessoa is not None:
            # Itera sobre todas as pessoas fornecidas
            for p in pessoa:
                # Imprime uma saudação para cada pessoa
                print("Olá,", p)

# Instanciação da classe Lar
batendoNaPorta = Lar()

# Chamada do método toctoc com dois nomes de pessoas
batendoNaPorta.toctoc("Ricky", "Morty")

# Chamada do método toctoc com um nome de pessoa
batendoNaPorta.toctoc("Rita Lee")