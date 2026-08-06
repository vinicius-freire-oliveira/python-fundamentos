from math import sqrt

numeros = [2, 8, 15, 23, 91, 112, 256]
# iniciando uma lista vazia para receber as raízes
raiz = []

# laço for para calcular cada raiz da lista de números e adicionar a lista raiz
for numero in numeros:
  raiz.append(sqrt(numero))

# laço for para ler a lista raiz e exibir um texto só quando a raiz for um valor inteiro 
for i in range(len(raiz)):
  # condição para testar se um número é inteiro (Ex: 2.5 // 1 = 2 ... 2 != 2.5)
  if raiz[i] // 1 == raiz[i]:
    print(f"O número {numeros[i]} possui raiz quadrada inteira igual a {int(raiz[i])}")
