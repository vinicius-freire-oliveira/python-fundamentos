# Menu com 5 opções que se repete com a escolha do usuário
while True:
    menu_list = ["Alugar um carro", "Devolver o carro"]
    for i, menu in enumerate(menu_list):
        print("[{}] {}".format(i, menu))
    conf = input("Digite sua opção: ")

    if(conf == "0"):
        print("Você quer alugar qual carro? ")
    elif(conf == "1"):
        print("Qual carro da lista você quer devolver? ")
    print("=" * 8)
    print("Digite 0 - para continuar | 1 para sair")

    if float(input()) == 1:
        break