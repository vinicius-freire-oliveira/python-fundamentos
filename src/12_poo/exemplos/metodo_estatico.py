# Define a classe Pagamento
class Pagamento:
    # Define um método estático chamado calcular_pagamento, que recebe horas e taxa como parâmetros
    @staticmethod
    def calcular_pagamento(horas, taxa):
        # Retorna o valor do pagamento calculado multiplicando as horas trabalhadas pela taxa
        return horas * taxa

# Chama o método estático calcular_pagamento da classe Pagamento com os argumentos 40 e 15
# Isso calcula o pagamento para 40 horas de trabalho com uma taxa horária de 15
# e imprime o resultado
print(Pagamento.calcular_pagamento(40, 15))
