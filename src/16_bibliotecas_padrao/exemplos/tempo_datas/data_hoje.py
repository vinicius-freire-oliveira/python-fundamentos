# Define a classe DATE
class DATA:
    # Define o método de inicialização com os parâmetros dd (dia), mm (mês) e yyyy (ano)
    def __init__(self, dd, mm, yyyy):
        # Atribui os valores passados como argumentos aos atributos da classe
        self.dia = dd
        self.mes = mm
        self.ano = yyyy

    # Define o método 'formated' para formatar a data
    def formatada(self):
        # Dicionário para converter o número do mês para o nome do mês
        mes_nome = {
            '1': 'janeiro',
            '2': 'fevereiro',
            '3': 'março',
            '4': 'abril',
            '5': 'maio',
            '6': 'junho',
            '7': 'julho',
            '8': 'agosto',
            '9': 'setembro',
            '10': 'outubro',
            '11': 'novembro',
            '12': 'dezembro'        
        }
        
        # Formata a data numericamente no formato 'dd/mm/yyyy'
        numerico = f'{self.dia:02d}/{self.mes:02d}/{self.ano:04d}'
        
        # Formata a data escrita no formato 'dd de mês de yyyy'
        extenso = f'{str(self.dia)} de {mes_nome[str(self.mes)]} de {str(self.ano)}'
        
        # Concatena as formas numérica e escrita da data com um separador e imprime o resultado
        ret = numerico + ' - ' + extenso
        print(ret)
        
        # Retorna a string formatada
        return ret

# Cria uma instância da classe DATE com os valores 28 (dia), 3 (mês) e 2019 (ano)
nova_data = DATA(28, 3, 2019)

# Chama o método 'formated' da instância criada para formatar e imprimir a data
nova_data.formatada()