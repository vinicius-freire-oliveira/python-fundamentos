def mdc(a, b):
    # Caso base: se b for igual a 0, retorna a
    if b == 0:
        return a
    # Caso recursivo: chama a função mdc com b e o resto da divisão de a por b
    return mdc(b, a % b)

# Testes da função mdc com diferentes pares de números
print(f"MDC 10 e 5 -->  {mdc(10,5)}")
print(f"MDC 32 e 24 --> {mdc(32,24)}")
print(f"MDC 5 e 3 -->   {mdc(5,3)}")
