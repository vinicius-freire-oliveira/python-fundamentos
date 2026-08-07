def media(lista: list=[0]) -> float:
    ''' Função para calcular a média de notas passadas por uma lista

    lista: list, default [0]
        Lista com as notas para calcular a média
    return = calculo: float
        Média calculada
    '''
    # Calcula a média das notas na lista
    calculo = sum(lista) / len(lista)

    # Levanta um erro se a lista tiver mais de 4 notas
    if len(lista) > 4:
        raise ValueError("A lista não pode possuir mais de 4 notas.")

    # Retorna o cálculo da média
    return calculo

# Primeiro bloco try-except-else-finally para testar a função 'media' com uma lista válida de 4 notas
try:
    # Define uma lista de notas
    notas = [6, 7, 8, 9]
    # Calcula a média das notas
    resultado = media(notas)
# Captura a exceção TypeError e imprime uma mensagem se ocorrer
except TypeError:
    print("Não foi possível calcular a média do(a) estudante. Só são aceitos valores numéricos!")
# Captura a exceção ValueError e imprime a mensagem de erro se ocorrer
except ValueError as e:
    print(e)
# Executa se nenhuma exceção foi lançada no bloco try
else:
    # Imprime o resultado da média
    print(resultado)
# Executa independentemente de uma exceção ter sido lançada ou não
finally:
    # Imprime uma mensagem indicando que a consulta foi encerrada
    print("A consulta foi encerrada!")

# Segundo bloco try-except-else-finally para testar a função 'media' com uma lista inválida de 5 notas
try:
    # Define uma lista de notas
    notas = [6, 7, 8, 9, 8]
    # Calcula a média das notas
    resultado = media(notas)
# Captura a exceção TypeError e imprime uma mensagem se ocorrer
except TypeError:
    print("Não foi possível calcular a média do(a) estudante. Só são aceitos valores numéricos!")
# Captura a exceção ValueError e imprime a mensagem de erro se ocorrer
except ValueError as e:
    print(e)
# Executa se nenhuma exceção foi lançada no bloco try
else:
    # Imprime o resultado da média
    print(resultado)
# Executa independentemente de uma exceção ter sido lançada ou não
finally:
    # Imprime uma mensagem indicando que a consulta foi encerrada
    print("A consulta foi encerrada!")

# Terceiro bloco try-except-else-finally para testar a função 'media' com uma lista contendo um valor não numérico
try:
    # Define uma lista de notas
    notas = [6, 7, 8, "9"]
    # Calcula a média das notas
    resultado = media(notas)
# Captura a exceção TypeError e imprime uma mensagem se ocorrer
except TypeError:
    print("Não foi possível calcular a média do(a) estudante. Só são aceitos valores numéricos!")
# Captura a exceção ValueError e imprime a mensagem de erro se ocorrer
except ValueError as e:
    print(e)
# Executa se nenhuma exceção foi lançada no bloco try
else:
    # Imprime o resultado da média
    print(resultado)
# Executa independentemente de uma exceção ter sido lançada ou não
finally:
    # Imprime uma mensagem indicando que a consulta foi encerrada
    print("A consulta foi encerrada!")
