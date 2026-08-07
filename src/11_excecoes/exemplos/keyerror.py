# Dicionário com nomes e idades correspondentes
idades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}

try:
    # Solicita ao usuário que digite um nome para buscar no dicionário
    chave = input()

    # Tenta acessar o valor no dicionário usando a chave fornecida pelo usuário
    valor = idades[chave]

# Captura uma exceção específica, neste caso KeyError, que ocorre quando a chave não existe no dicionário
except KeyError:
    # Se a chave não for encontrada, imprime uma mensagem de erro
    print('Nome não encontrado')

# Se não ocorrer exceção no bloco try, executa o bloco else
else:
    # Imprime o valor correspondente à chave encontrada no dicionário
    print(valor)

