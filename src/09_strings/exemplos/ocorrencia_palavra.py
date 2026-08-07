def contar_ocorrencias_palavras(frase):
    # Divide a frase em palavras usando espaços como delimitadores
    palavras = frase.split()

    # Cria um dicionário para armazenar a contagem de cada palavra
    contagem = {}

    # Itera sobre cada palavra na lista de palavras
    for palavra in palavras:
        # Converte a palavra para minúscula para contagem case-insensitive
        palavra = palavra.lower()
        # Se a palavra já estiver no dicionário, incrementa a contagem
        if palavra in contagem:
            contagem[palavra] += 1
        # Se a palavra não estiver no dicionário, adiciona com contagem 1
        else:
            contagem[palavra] = 1

    return contagem

def main():
    # Solicita ao usuário que insira uma frase
    frase = input("Digite uma frase: ")

    # Chama a função de contagem de ocorrências de palavras
    contagem = contar_ocorrencias_palavras(frase)

    # Imprime os resultados
    print("Ocorrência de palavras:")
    for palavra, qtd in contagem.items():
        print(f"{palavra}: {qtd}")

# Executa a função principal quando o script é executado
if __name__ == "__main__":
    main()
