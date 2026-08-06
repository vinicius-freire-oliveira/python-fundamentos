# Definindo uma variável global
variavel_global = 10

# Definindo uma função que usa a variável global
def funcao_global():
    # A variável global pode ser acessada e modificada dentro da função
    global variavel_global
    print("Dentro da função global, variavel_global =", variavel_global)
    variavel_global = 20  # Modificando o valor da variável global
    
# Chamando a função
funcao_global()

# Imprimindo o valor da variável global após a chamada da função
print("Fora da função global, variavel_global =", variavel_global)