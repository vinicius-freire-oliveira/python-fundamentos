import math

# Função para calcular as raízes usando a fórmula de Bhaskara
def calcular_bhaskara(a, b, c):
    # Calculando o discriminante
    delta = b**2 - 4*a*c
    
    # Verificando se o discriminante é válido
    if delta < 0:
        print("O delta é negativo. A equação não tem raízes reais.")
    else:
        # Calculando as raízes
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"As raízes da equação são: x1 = {x1}, x2 = {x2}")

# Solicitando os coeficientes ao usuário
a = float(input("Informe o valor de a: "))
b = float(input("Informe o valor de b: "))
c = float(input("Informe o valor de c: "))

# Chamando a função para calcular as raízes
calcular_bhaskara(a, b, c)
