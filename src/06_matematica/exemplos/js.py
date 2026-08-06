# Define a função para calcular juros simples
def js():
    # Solicita ao usuário que insira os valores do capital, taxa de juros e tempo
    c = float(input("Capital: "))
    i = float(input("Taxa de juros a.a: "))
    t = int(input("Tempo em anos: "))
    
    # Calcula os juros simples utilizando a fórmula J = (C * i * t) / 100
    j = (c * i * t) / 100
    
    # Imprime o valor dos juros formatado com duas casas decimais
    print("O valor do juros é R$ {:.2f}".format(j))

# Chama a função js para calcular e imprimir os juros simples
js()
