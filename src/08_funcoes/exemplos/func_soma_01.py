# Criando uma função
def funcao_soma():
    valor1 = int(input("Digite um valor: "))
    valor2 = int(input("Digite um valor: "))
    valor = valor1 + valor2

    print("A soma desses números é: {}".format(valor))

    if valor % 2 == 0:
        print("{} é par!".format(valor))
    else:
        print("{} é ímpar!".format(valor))

funcao_soma()