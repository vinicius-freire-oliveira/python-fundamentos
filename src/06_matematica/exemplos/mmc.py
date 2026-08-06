def mdc(a, b):
    # Função para calcular o MDC utilizando o algoritmo de Euclides
    if b == 0:
        return a
    return mdc(b, a % b)

def mmc(a, b):
    # Função para calcular o MMC utilizando o MDC e a fórmula: |a * b| / mdc(a, b)
    return abs(a * b) / mdc(a, b)

# Exemplos de uso
print(f"MMC de 10 e 5 é: {mmc(10, 5)}")
print(f"MMC de 32 e 24 é: {mmc(32, 24)}")
print(f"MMC de 5 e 3 é: {mmc(5, 3)}")
