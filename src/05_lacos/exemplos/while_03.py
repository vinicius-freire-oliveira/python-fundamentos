# Laço de repetição while com continue
x = 0
while x < 10:
    print("O valor de x é: {}".format(x))
    x = x + 1
    continue # Interrompe um loop e vai para a próxima execução do loop
    print("x ainda é menor que 10, incrementando...")
else:
    print("Concluído")