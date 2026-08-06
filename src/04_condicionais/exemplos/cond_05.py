# Criar um RPG
seuNome = str(input("Digite seu nome: "))

print("Bem-vindo ao Fuctura Game,", seuNome, "!!")
print("Você está em uma caverna e a primeira que coisa que vê são 3 itens: ")
print("Uma espada, um arco e um cajado, qual deseja pegar?")

arma = str(input("Digite 1 para espada, 2 para arco e 3 para cajado: "))

if(arma == "1"):
    print("Você se tornou um guerreiro! e apareceu um goblin na sua frente")
    print("O que deseja fazer? digite 1 para atacar ou 2 para fugir")
    acao = str(input("Digite aqui a sua ação: "))
    if(acao == "1"):
        print("Você atacou o goblin, mas ele tinha amigos e lhe matou")
    elif(acao =="2"):
        print("Você não conseguiu fugir e infelizmente levou uma flechada")
    else:
        print("Você não escolheu a ação correta, os deuses não lhe ajudarão")
elif(arma =="2"):
    print("Você se tornou um arqueiro!")
    print("Apareceu uma cobra na sua frente o que você vai fazer?")
    acao = str(input("Digite 1 para fugir ou 2 para atacar"))
    if(acao == "1"):
        print("Você conseguiu fugir mas infelizmente...")
        print("Mas infelizmente caiu em um buraco e morreu")
    elif(acao == "2"):
        print("Você conseguiu atacar..., porém...")
        print("Percebeu que não tinha flechas e a cobra lhe picou")
        print("E você morreu")
    else:
        print("Você não escolheu a ação correta, os deuses não lhe ajudarão")