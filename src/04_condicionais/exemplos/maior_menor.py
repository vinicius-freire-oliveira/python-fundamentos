# Inicializa as variáveis maior e menor com valores iniciais
maior = 0
menor = 1000

# Loop para solicitar os pesos de 5 pessoas
for c in range(1, 6):
    # Solicita o peso da pessoa atual
    n = int(input('Digite o peso da {}ª pessoa: '.format(c)))
    
    # Verifica se o peso atual é o maior encontrado até agora
    if n > maior:
        maior = n
    
    # Verifica se o peso atual é o menor encontrado até agora
    if n < menor:
        menor = n

# Imprime o menor e o maior peso
print('O menor peso é {}Kg e o maior peso é {}Kg'.format(menor, maior))
