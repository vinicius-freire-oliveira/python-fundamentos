# Solicita ao usuário que digite as três notas do estudante e as converte para float
N1 = float(input("Digite a 1ª nota do(a) estudante: "))
N2 = float(input("Digite a 2ª nota do(a) estudante: "))
N3 = float(input("Digite a 3ª nota do(a) estudante: "))

# Define uma função lambda chamada media_ponderavel, que calcula a média ponderada das notas fornecidas
media_ponderavel = lambda x, y, z: (x * 3 + y * 2 + z * 5) / 10

# Calcula a média ponderada do estudante utilizando a função lambda media_ponderavel
media_estudante = media_ponderavel(N1, N2, N3)

# Imprime a média ponderada calculada
print(media_estudante)
