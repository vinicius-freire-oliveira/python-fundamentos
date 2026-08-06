# Definindo uma função que cria uma variável local
def funcao_local():
    variavel_local = 5
    print("Dentro da função local, variavel_local =", variavel_local)
    return variavel_local

# Chamando a função e atribuindo seu retorno a uma variável global
variavel_local_fora = funcao_local()

# Agora podemos usar a variável global
print("Fora da função local, variavel_local_fora =", variavel_local_fora)