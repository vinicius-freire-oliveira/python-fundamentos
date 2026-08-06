termos = int(input("Digite a quantidade de termos para calcular: "))  

# Começando com 0 e 1
num1, num2 = 0, 1
contador = 0

# Executa a sequência de Fibonacci até atingir a quantidade de termos especificada
while contador < termos:
    num3 = num1 + num2  # Calcula o próximo termo
    # Atualiza os valores para os próximos cálculos
    num1 = num2
    num2 = num3
    contador += 1
    print(num1)  # Imprime o termo atual da sequência 
