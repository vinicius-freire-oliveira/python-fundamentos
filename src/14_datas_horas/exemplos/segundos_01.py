class ConversorTempo:
    def __init__(self, dias, horas, minutos, segundos):
        self.dias = dias
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos

    def converter_para_segundos(self):
        total_segundos = self.dias * 24 * 3600 + self.horas * 3600 + self.minutos * 60 + self.segundos
        return total_segundos

# Solicita ao usuário que insira os valores de dias, horas, minutos e segundos
dias = int(input("Digite o número de dias: "))
horas = int(input("Digite o número de horas: "))
minutos = int(input("Digite o número de minutos: "))
segundos = int(input("Digite o número de segundos: "))

# Cria uma instância da classe ConversorTempo com os valores fornecidos pelo usuário
conversor = ConversorTempo(dias, horas, minutos, segundos)

# Realiza a conversão e imprime o resultado
total_segundos = conversor.converter_para_segundos()
print("Tempo em segundos:", total_segundos)
