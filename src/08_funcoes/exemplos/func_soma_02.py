# Criando uma função
def funcao_soma(valor1, valor2): # Criando uma função com dois argumentos obrigatórios
    valor = valor1 + valor2

    print("A soma desses números é: {}".format(valor))

    if valor % 2 == 0:
        print("{} é par!".format(valor))
    else:
        print("{} é ímpar!".format(valor))
    return(valor) #Retorno do valor da operação caso sua função ou método precise

funcao_soma(2,3) # Dois argumentos são obrigatórios!