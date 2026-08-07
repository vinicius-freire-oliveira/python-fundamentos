# Solicita ao usuário que insira uma palavra e remove os espaços em branco no início e no final da string,
# além de converter todas as letras para maiúsculas.
palavra = str(input('Digite uma palavra: ')).strip().upper()

# Inverte a palavra utilizando a técnica de fatiamento de string.
inverso = palavra[::-1]

# Verifica se o inverso da palavra é diferente da palavra original.
if inverso != palavra:
    # Se forem diferentes, imprime que a palavra não é um palíndromo.
    print('A frase: {} não é um Palíndromo, pois '.format(palavra))
    # Imprime as versões original e invertida da palavra.
    print('{} é diferente de {}'.format(palavra, inverso))
else:
    # Se forem iguais, imprime que a palavra é um palíndromo.
    print('A frase: {} é um Palíndromo, pois'.format(palavra))
    # Imprime as versões original e invertida da palavra.
    print('{} é igual a {}'.format(palavra, inverso))
