idades = [20, 39, 18, 27, 19]

def proximo_ano(idade):
    return idade+1

""" Esta é uma lista de compreensão que aplica a função "proximo_ano" a cada elemento da lista "idades" que é maior que 21. O resultado é uma nova lista com as idades maiores que 21 incrementadas em 1. No caso da lista "idades", o resultado será [40, 28]. """
print([proximo_ano(idade) for idade in idades if idade > 21])

# Esta é uma função chamada "faz_processamento_de_visualizacao" que recebe um parâmetro "lista", imprime o tamanho da lista e adiciona o valor 13 ao final da lista.
def faz_processamento_de_visualizacao(lista):
  print(len(lista))
  lista.append(13)

"""A função "faz_processamento_de_visualizacao" é chamada com a lista "idades" como argumento, imprime o tamanho da lista (5) e adiciona o valor 13 ao final da lista. Em seguida, a lista "idades" é impressa novamente, resultando na lista [16, 21, 29, 56, 43, 13]."""  
idades = [16, 21, 29, 56, 43]

faz_processamento_de_visualizacao(idades)
print(idades)

"""Se nenhum argumento for passado quando a função é chamada, a lista padrão vazia será usada. A função imprime o tamanho da lista e adiciona o valor 13 ao final da lista."""
def faz_processamento_de_visualizacao(lista = []):
  print(len(lista))
  print(lista)
  lista.append(13)

""" A função "faz_processamento_de_visualizacao" é chamada várias vezes sem passar argumentos. Como a lista padrão é compartilhada entre as chamadas, o valor 13 é adicionado à lista padrão a cada chamada. """
faz_processamento_de_visualizacao()

faz_processamento_de_visualizacao()

faz_processamento_de_visualizacao()

faz_processamento_de_visualizacao()

"""Este é outro exemplo de uma função com um parâmetro padrão, mas desta vez usando a função "list()" como valor padrão. Essencialmente, é a mesma situação que a anterior, e os resultados serão os mesmos:"""
def faz_processamento_de_visualizacao(lista = list()):
  print(len(lista))
  print(lista)
  lista.append(13)

faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()

"""Se nenhum argumento for passado, a lista "lista" será inicializada como uma lista vazia. Isso evita o compartilhamento da mesma lista em chamadas subsequentes. A saída será uma lista vazia sempre com índice 0."""
def faz_processamento_de_visualizacao(lista = None):
  if lista == None:
    lista = list()
  print(len(lista))
  print(lista)
  lista.append(13)

faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()