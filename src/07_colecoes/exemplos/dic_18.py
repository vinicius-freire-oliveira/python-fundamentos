# Cria um dicionário padrão chamado 'aparicoes' com alguns valores iniciais
aparicoes = {
  "Guilherme": 1,
  "cachorro": 2,
  "nome": 2,
  "vindo": 1
}

# Um texto exemplo que será analisado para contar as palavras
meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"

# Importa a classe defaultdict do módulo collections
from collections import defaultdict

# Cria um defaultdict chamado 'aparicoes' que retorna 0 quando uma nova chave é acessada
aparicoes = defaultdict(int)

# Itera sobre cada palavra no texto dividido em palavras
for palavra in meu_texto.split():
  # Incrementa a contagem da palavra em 1
  aparicoes[palavra] += 1

# Imprime o dicionário de aparições de palavras
print(aparicoes)

# Define uma classe simples chamada 'Conta' que imprime uma mensagem quando uma instância é criada
class Conta:
  def __init__(self):
    print("Criando uma conta")

# Cria um defaultdict chamado 'contas' que cria uma nova instância de 'Conta' quando uma nova chave é acessada
contas = defaultdict(Conta)

# Acessa a chave '15' no dicionário 'contas', criando uma nova instância de 'Conta' e imprimindo a mensagem
print(contas[15])

# Acessa a chave '17' no dicionário 'contas', criando outra nova instância de 'Conta' e imprimindo a mensagem
print(contas[17])

# Acessa novamente a chave '15' no dicionário 'contas', desta vez não cria uma nova instância porque já existe uma
print(contas[15])

# Importa a classe Counter do módulo collections
from collections import Counter

# Cria um Counter chamado 'aparicoes'
aparicoes = Counter()

# Itera sobre cada palavra no texto dividido em palavras
for palavra in meu_texto.split():
  # Incrementa a contagem da palavra em 1
  aparicoes[palavra] += 1

# Imprime o Counter de aparições de palavras
print(aparicoes)

# Outra maneira de inicializar um Counter diretamente com a lista de palavras
aparicoes = Counter(meu_texto.split())

# Imprime o Counter de aparições de palavras
print(aparicoes)

