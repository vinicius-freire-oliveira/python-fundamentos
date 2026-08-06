# Inicializa o contador como 1
contador = 1

# Inicia um loop while que continua enquanto o contador for menor ou igual a 10
while(contador <= 10):
    # Imprime o valor atual do contador
    print(contador)
    # Incrementa o contador em 3 para o próximo ciclo
    contador = contador + 3

# Mesmo resultado usando um loop for
# O loop for percorre a faixa de 1 a 10 com um passo de 3
# Ou seja, ele começa em 1, pula de 3 em 3, e termina antes de chegar a 10
for contador in range(1, 11, 3):
    # Imprime o valor atual do contador
    print(contador)
