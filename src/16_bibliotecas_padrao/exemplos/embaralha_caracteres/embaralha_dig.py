# Importa a função shuffle do módulo random
from random import shuffle

# Define a função 'embaralha' que recebe um parâmetro 'nome'
def embaralha(nome):
    # Converte a string 'nome' em uma lista de caracteres
    a = list(nome)
    
    # Embaralha os elementos da lista 'a'
    shuffle(a)
    
    # Junta os caracteres embaralhados em uma única string
    a = ''.join(a)
    
    # Converte a string resultante para minúsculas e imprime o resultado
    print(a.lower())

# Solicita ao usuário para digitar algo e armazena na variável 'nome'
nome = input('Digite algo: ')

# Chama a função 'embaralha' com o valor digitado pelo usuário como argumento
embaralha(nome)
