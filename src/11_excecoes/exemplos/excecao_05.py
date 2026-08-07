# Define um dicionário com nomes de funcionários e seus respectivos salários
funcionarios = {'José': 2000, 'Ana': 2200, 'João': 2500, 'Maria': 3800}

# Inicia um bloco try para capturar possíveis exceções
try:
    # Aplica um aumento de 10% aos salários usando a função map e uma função lambda
    # A função lambda multiplica cada valor do dicionário por 1.1
    aumento = list(map(lambda x: x * 1.1, funcionarios.values()))

# Captura qualquer exceção que ocorra no bloco try
except Exception as e:
    # Imprime o tipo da exceção e a mensagem de erro
    print(type(e), f'Erro: {e}')

# Executa este bloco se nenhum erro ocorreu no bloco try
else:
    # Imprime a lista de salários aumentados
    print(aumento)

# Executa este bloco independentemente de ter ocorrido um erro ou não
finally:
    # Imprime uma mensagem indicando que o processo foi concluído
    print("Processo concluído!")
