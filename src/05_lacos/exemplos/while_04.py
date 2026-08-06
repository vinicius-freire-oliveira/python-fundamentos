# Laço de repetição while com break
x = 0
while x < 10:
    print("O valor de x é: {}".format(x))
    x = x + 1
    break # Interrompe um loop e encerra ele
    print("x ainda é menor que 10, incrementando...")
else:
    print("Concluído")