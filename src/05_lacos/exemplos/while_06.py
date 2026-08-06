# Laço while True, interrompe com break
while True:
    c = input("Digite 1 para parar | Digite 0 para continuar: ")
    if c == "1":
        print("Fechando...")
        break
    else:
        print("Repetindo...")