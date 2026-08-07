# Criar um sistema de Imposto de Renda simples

# Definição da classe PessoaFisica para representar pessoas físicas
class PessoaFisica():
    def __init__(self, nome, salario):
        # Inicialização dos atributos da instância com os valores fornecidos
        self.nome = nome
        self.salario = salario
    
    # Método para calcular e imprimir o imposto de renda de uma pessoa física
    def impostoDeRenda(self):
        irrf = self.salario * 0.03
        print(f'{self.nome}, seu salário é R$ {self.salario} e seu IRRF é R$ {irrf}')

# Definição da classe PessoaJuridica para representar pessoas jurídicas
class PessoaJuridica():
    def __init__(self, razaoSocial, faturamento):
        # Inicialização dos atributos da instância com os valores fornecidos
        self.razaoSocial = razaoSocial
        self.faturamento = faturamento

    # Método para calcular e imprimir o imposto de renda de uma pessoa jurídica
    def impostoDeRendaPJ(self):
        irpj = self.faturamento * 0.1
        print(f'{self.razaoSocial}, o faturamento da empresa é R$ {self.faturamento} e o seu IRPJ é R$ {irpj}')

# Loop principal do programa
while True:
    print("Escolha a opção 0 - Pessoa Física | 1 - Pessoa Jurídica: ")
    conf = int(input()) # Solicita ao usuário para escolher o tipo de contribuinte
    if conf == 0: # Se a escolha for 0, solicita informações de uma pessoa física
        nome = input("Digite seu nome: ")
        salario = float(input("Digite seu salário: "))
        in1 = PessoaFisica(nome, salario) # Cria uma instância da classe PessoaFisica
        in1.impostoDeRenda() # Chama o método impostoDeRenda() para calcular e imprimir o imposto de renda da pessoa física
    elif conf == 1: # Se a escolha for 1, solicita informações de uma pessoa jurídica
        razaoSocial = input("Digite a razão social da empresa: ")
        faturamento = float(input("Digite o faturamento da empresa: "))
        in2 = PessoaJuridica(razaoSocial, faturamento) # Cria uma instância da classe PessoaJuridica
        in2.impostoDeRendaPJ() # Chama o método impostoDeRendaPJ() para calcular e imprimir o imposto de renda da pessoa jurídica

        print("") # Adiciona uma linha em branco
        print("0 - Continuar | 1 - Sair") # Solicita ao usuário para continuar ou sair do programa

        if int(input()) == 1: # Se a entrada do usuário for 1, encerra o loop
            break # Sai do loop e encerra o programa
