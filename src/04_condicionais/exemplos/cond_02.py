# Criar um sistema que valide um cupom de 15% e de 10%,
#e se o cupom não for válido informar o usuário
cupom = str(input("Digite aqui o seu cupom: "))

if(cupom == "Fuctura1"):
    print("\nVocê ganhou 15% de desconto!!!")
elif(cupom == "Fuctura2"): # estrutura entre if e else
    print("\nVocê ganhou 10% de desconto!!!")
else: # termina a condição
    print("\nEsse cupom não é válido")