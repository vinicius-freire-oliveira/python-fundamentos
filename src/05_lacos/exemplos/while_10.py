# Laço de repetição com while
s = "String"
indice = 0
while indice in range(len(s)):
    # Imprime o elemento da string correspondente ao índice atual.
    print("Estamos no elemento", s[indice]) # Dentro do loop, a cada iteração, este trecho imprime o caractere atual da string s.
    indice += 1

