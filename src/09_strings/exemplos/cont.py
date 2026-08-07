# Função para contar o número total de caracteres na frase
def contar_caracteres(frase):
    return len(frase)

# Função para contar o número de palavras na frase
def contar_palavras(frase):
    palavras = frase.split()  # Divide a frase em palavras usando espaços como delimitador
    return len(palavras)

# Função para contar o número de espaços na frase
def contar_espacos(frase):
    return frase.count(' ')  # Conta quantos espaços existem na frase

# Função para contar o número de linhas na frase
def contar_linhas(frase):
    linhas = frase.split('\n')  # Divide a frase em linhas usando '\n' como delimitador
    return len(linhas)

# Função para contar o número de vogais na frase
def contar_vogais(frase):
    vogais = 'aeiouAEIOU'  # Define as vogais (maiúsculas e minúsculas)
    return sum(1 for char in frase if char in vogais)  # Conta quantos caracteres são vogais

# Função para contar o número de dígitos na frase
def contar_numeros(frase):
    return sum(1 for char in frase if char.isdigit())  # Conta quantos caracteres são dígitos

# Função principal do programa
def main():
    print("Digite uma frase (digite 'STOP' em uma nova linha para finalizar a entrada):")
    
    linhas = []
    while True:
        linha = input()
        if linha.strip().upper() == 'STOP':
            break
        linhas.append(linha)
    
    frase = '\n'.join(linhas)
    
    # Chama as funções de contagem e armazena os resultados
    qtd_caracteres = contar_caracteres(frase)
    qtd_palavras = contar_palavras(frase)
    qtd_espacos = contar_espacos(frase)
    qtd_linhas = contar_linhas(frase)
    qtd_vogais = contar_vogais(frase)
    qtd_numeros = contar_numeros(frase)

    # Imprime os resultados das contagens
    print(f"Quantidade de caracteres: {qtd_caracteres}")
    print(f"Quantidade de palavras: {qtd_palavras}")
    print(f"Quantidade de espaços: {qtd_espacos}")
    print(f"Quantidade de linhas: {qtd_linhas}")
    print(f"Quantidade de vogais: {qtd_vogais}")
    print(f"Quantidade de números: {qtd_numeros}")

# Função de teste para verificar a contagem de linhas
def teste_contar_linhas():
    # Teste com múltiplas linhas
    frase_teste = "Esta é a primeira linha.\nEsta é a segunda linha.\nEsta é a terceira linha."
    resultado = contar_linhas(frase_teste)

# Executa a função principal quando o script é executado
if __name__ == "__main__":
    main()
    teste_contar_linhas()
