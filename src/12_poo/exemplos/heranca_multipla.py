# Definição da classe base Funcionario
class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas registradas.')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

# Definição da classe Caelum que herda de Funcionario
class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

# Definição da classe Alura que herda de Funcionario
class Alura(Funcionario):
    # Sobrescrevendo o método mostrar_tarefas da classe base
    # def mostrar_tarefas(self):
    #     print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')

# Definição da classe Hipster, que serve como classe mista sem herança de Funcionario
class Hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'

# Definição da classe Junior que herda de Alura
class Junior(Alura):
    pass

# Definição da classe Pleno que herda de Alura, Caelum e Hipster
class Pleno(Alura, Caelum, Hipster):
    pass

# Instância da classe Junior com o nome 'José'
jose = Junior('José')

# Utilização de métodos da classe Junior e da classe Alura
jose.busca_perguntas_sem_resposta()
jose.mostrar_tarefas()

# Instância da classe Pleno com o nome 'Luan'
luan = Pleno('Luan')

# Utilização de métodos das classes Pleno, Alura e Caelum
luan.busca_perguntas_sem_resposta()
luan.busca_cursos_do_mes()

# O método mostrar_tarefas é herdado da classe Alura e sobrescrito pela classe Caelum na classe Pleno
luan.mostrar_tarefas()

# Impressão do objeto luan, que utiliza o método __str__ da classe Hipster
print(luan)
