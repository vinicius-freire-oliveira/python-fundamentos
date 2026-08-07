import inflect  # Importa a biblioteca inflect, usada para converter números em palavras em inglês
from num2words import num2words  # Importa a função num2words da biblioteca num2words para converter números em palavras em várias línguas

# Função para converter um número para palavras
def numero_por_extenso(numero, lingua='pt'):
    if lingua == 'pt':
        return num2words(numero, lang='pt')  # Converte o número para palavras em português
    elif lingua == 'en':
        p = inflect.engine()  # Cria uma instância do motor inflect
        return p.number_to_words(numero)  # Converte o número para palavras em inglês

# Função para mostrar o menu de opções ao usuário
def mostrar_menu():
    print("Escolha a língua para a conversão:")
    print("1 - Português")
    print("2 - Inglês")
    print("Digite 'sair' para encerrar o programa.")

# Função principal que executa o loop do programa
def main():
    while True:
        mostrar_menu()  # Mostra o menu de opções
        escolha_lingua = input("Escolha uma opção (1-2): ")  # Pede ao usuário para escolher a língua
        
        if escolha_lingua.lower() == 'sair':
            break  # Sai do loop se o usuário digitar 'sair'
        
        if escolha_lingua not in ['1', '2']:
            print("Opção inválida. Tente novamente.")  # Informa ao usuário que a opção é inválida
            continue  # Volta ao início do loop

        lingua = 'pt' if escolha_lingua == '1' else 'en'  # Define a língua com base na escolha do usuário

        entrada = input("Digite um número (ou 'sair' para encerrar): ")  # Pede ao usuário para digitar um número
        if entrada.lower() == 'sair':
            break  # Sai do loop se o usuário digitar 'sair'

        try:
            numero = int(entrada)  # Converte a entrada para um número inteiro
            resultado = numero_por_extenso(numero, lingua)  # Converte o número para palavras na língua escolhida
            lingua_texto = "português" if lingua == 'pt' else "inglês"  # Define a língua para exibir na mensagem
            print(f"O número {numero} por extenso em {lingua_texto} é: {resultado}")  # Imprime o resultado
        except ValueError:
            print("Por favor, digite um número válido.")  # Informa ao usuário que a entrada não é um número válido

# Executa a função principal se o script for executado diretamente
if __name__ == "__main__":
    main()
