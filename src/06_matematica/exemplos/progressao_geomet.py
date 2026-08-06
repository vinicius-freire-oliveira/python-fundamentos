def pg():
    a1 = int(input("Primeiro termo: "))
    n = int(input("Número de termos: "))
    q = int(input("Razão: "))
    an = a1 * q ** (n - 1)
    print("Último termo:", an)

pg() 
