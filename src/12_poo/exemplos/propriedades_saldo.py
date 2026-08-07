# Define a classe Conta
class Conta:
    # Método construtor para inicializar os atributos numero, titular, saldo e limite
    def __init__(self, numero, titular, saldo, limite):
        # Imprime uma mensagem indicando que um objeto está sendo construído
        print("Construindo objeto ...{}".format(self))
        # Atributo privado __numero para armazenar o número da conta
        self.__numero = numero
        # Atributo privado __titular para armazenar o titular da conta
        self.__titular = titular
        # Atributo privado __saldo para armazenar o saldo da conta
        self.__saldo = saldo
        # Atributo privado __limite para armazenar o limite da conta
        self.__limite = limite

    # Métodos para obter o saldo e o titular da conta
    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    # Propriedade 'limite' com getter e setter
    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    # Propriedade 'saldo' com getter e setter
    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

# Cria uma instância da classe Conta com os parâmetros especificados
conta = Conta(1, "Abreu", 50.0, 2000.0)

# Imprime o saldo da conta usando a propriedade 'saldo'
print(conta.saldo)  # Saída: 50.0
