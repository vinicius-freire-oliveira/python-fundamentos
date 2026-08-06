# Variável global
valor = 20

def funcao_soma1(valor1, valor2):
    valor = valor1 + valor2
    print("A soma desses números é: {}".format(valor))

    if valor % 2 == 0:
        print("{} é par!".format(valor))
    else:
        print("{} é ímpar!".format(valor))
    return(valor)

funcao_soma1(10,30)

print("O valor da variável global é: ", valor)