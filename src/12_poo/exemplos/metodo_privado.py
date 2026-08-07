# Define a classe Apresentacao
class Apresentacao:
    # Método construtor para inicializar os atributos horario e banda
    def __init__(self, horario, banda):
        # Atributo privado __horario para armazenar o horário da apresentação
        self.__horario = horario
        # Atributo privado __banda para armazenar o nome da banda
        self.__banda = banda

    # Método getter para obter o horário da apresentação
    def get_horario(self):
        return self.__horario

    # Método setter para definir o horário da apresentação
    def set_horario(self, horario):
        self.__horario = horario

    # Método getter para obter o nome da banda
    def get_banda(self):
        return self.__banda

    # Método setter para definir o nome da banda
    def set_banda(self, banda):
        self.__banda = banda

# Criando uma instância da classe Apresentacao
apresentacao = Apresentacao("20:00", "Banda X")

# Obtendo e imprimindo o horário da apresentação
print(apresentacao.get_horario())  # Saída: 20:00

# Obtendo e imprimindo o nome da banda
print(apresentacao.get_banda())  # Saída: Banda X

# Definindo um novo horário para a apresentação
apresentacao.set_horario("21:30")

# Definindo um novo nome para a banda
apresentacao.set_banda("Banda Y")

# Obtendo e imprimindo o novo horário da apresentação
print(apresentacao.get_horario())  # Saída: 21:30

# Obtendo e imprimindo o novo nome da banda
print(apresentacao.get_banda())  # Saída: Banda Y
