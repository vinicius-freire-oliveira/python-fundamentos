def maiusculo(frase):
    # Converte a frase para letras maiúsculas
    return frase.upper()

def minusculo(frase):
    # Converte a frase para letras minúsculas
    return frase.lower()

def alternado(frase):
    # Converte a frase para letras alternadas entre maiúsculas e minúsculas
    resultado = ''
    maiuscula = True
    for char in frase:
        if char.isalpha():
            if maiuscula:
                resultado += char.upper()
            else:
                resultado += char.lower()
            maiuscula = not maiuscula
        else:
            resultado += char
    return resultado

def inverter(frase):
    # Inverte a ordem dos caracteres na frase
    return frase[::-1]

def primeira_letra_palavra(frase):
    # Converte a primeira letra de cada palavra para maiúscula
    palavras = frase.split()
    resultado = [palavra.capitalize() for palavra in palavras]
    return ' '.join(resultado)

def primeira_palavra_frase(frase):
    # Converte a primeira letra da primeira palavra de cada frase para maiúscula
    sentencas = frase.split('. ')
    resultado = [sentenca.capitalize() for sentenca in sentencas]
    return '. '.join(resultado)

def mostrar_menu():
    # Exibe o menu de opções para o usuário
    print("\nEscolha a formatação do texto:")
    print("1 - Maiúsculo")
    print("2 - Minúsculo")
    print("3 - Alternado")
    print("4 - Inverter")
    print("5 - Primeira letra de cada palavra")
    print("6 - Primeira palavra de cada frase")
    print("7 - Sair")

def main():
    # Solicita ao usuário que digite uma frase
    frase = input("Digite uma frase: ")

    while True:
        # Exibe o menu e solicita uma opção ao usuário
        mostrar_menu()
        opcao = int(input("Escolha uma opção (1-7): "))

        # Aplica a formatação escolhida pelo usuário
        if opcao == 1:
            resultado = maiusculo(frase)
        elif opcao == 2:
            resultado = minusculo(frase)
        elif opcao == 3:
            resultado = alternado(frase)
        elif opcao == 4:
            resultado = inverter(frase)
        elif opcao == 5:
            resultado = primeira_letra_palavra(frase)
        elif opcao == 6:
            resultado = primeira_palavra_frase(frase)
        elif opcao == 7:
            # Sai do programa se o usuário escolher a opção 7
            print("Saindo do programa.")
            break
        else:
            # Informa ao usuário que a opção é inválida
            resultado = "Opção inválida. Tente novamente."

        # Exibe o resultado da formatação
        print("\nResultado:")
        print(resultado)

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()
