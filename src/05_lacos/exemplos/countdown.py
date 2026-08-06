from time import sleep  # Importa a função sleep do módulo time

# Loop que conta de 10 até 1, com um passo de -1
for c in range(10, 0, -1):
    print(c)  # Imprime o valor atual de c
    sleep(1)  # Pausa a execução do programa por 1 segundo
print("O tempo acabou para você!!!!")  # Após o loop, imprime uma mensagem
