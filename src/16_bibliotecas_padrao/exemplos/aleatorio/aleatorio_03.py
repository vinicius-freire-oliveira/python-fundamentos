from random import randint
# Transformando a quantidade de participantes de string para inteiro
n = int(input("Digite o nº de participantes do sorteio: "))
# Sorteando um número no intervalo de 1 até a quantidade de participantes
print(f"O número sorteado foi {randint(1, n)}")
