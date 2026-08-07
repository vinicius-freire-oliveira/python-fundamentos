from random import choices

# Lista das frutas disponíveis
frutas = ["maçã", "banana", "uva", "pêra","manga", "coco", 
          "melancia", "mamão", "laranja", "abacaxi", "kiwi", "ameixa"]

# Gerando uma lista com a escolha aleatoria de 3 frutas 
salada = choices(frutas, k=3)

# Imprimindo os itens da lista de frutas gerada
print(f"A salada surpresa é: {salada[0]}, {salada[1]} e {salada[2]}")
