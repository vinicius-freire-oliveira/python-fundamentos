# Laço de repetição com while e loop infinito com .append
i = 0
elemento = [1,2,3,4,5,6]

print(type(elemento))

while i < len(elemento):
    print("O elemento é: ", elemento)
    elemento.append(i) # caso não tenha break o resultado será infinito
    i += 1
    break