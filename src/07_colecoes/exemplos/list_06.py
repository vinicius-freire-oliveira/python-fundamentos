# Fatiamento lista - Lista[star:stop:step] - 
# lista[início:fim ou parada:intervalo ou passo]
lista2 = list((1, "2", 3)) 
lista3 = ["C", 4.65, True, "True", "Vamos aprender", ["outra", "lista", "interna"], lista2]

print(lista3)
print(lista3[2:6:2]) # Começará do índice 2 até o índice 5, de dois em dois
print(lista3[:3]) # Ausência do início, indica fatiamento a partir do primeiro índice
print(lista3[1:]) # Ausência do fim, inicia o fatiamento a partir do índice indicado
print("Imprimindo de dois em dois: ", lista3[::2]) # Dois em dois
print(lista3[::]) # Toda a lista
print(lista3[-1]) # Último item da lista, a contagem de ídice negativo começa de trás para frente com -1
print(len(lista3[5][2])) # Tamanho da lista sem considerar o índice 0
print(lista3[5][2]) # Lista dentro de outra lista
print(len(lista3)) # Comprimento da lista