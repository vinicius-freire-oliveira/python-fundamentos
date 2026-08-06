# riar um sistema que valide um cupom, caso o 
# cupom não for válido informar o usuário
cupom = str(input("Digite aqui o seu cupom: "))

if(cupom == "Fuctura1" or cupom == "Fuctura2"):
    print("\nVocê ganhou 15% de desconto")
else:
    print("\nEsse cupom não é válido!")