# Solicita ao usuário que digite a nota do estudante e a converte para float
nota = float(input("Digite a nota do(a) estudante: "))

# Define uma função lambda chamada qualitativo, que adiciona 0.5 à nota fornecida
qualitativo = lambda x: x + 0.5

# Imprime o resultado da aplicação da função lambda qualitativo à nota digitada pelo usuário
print(qualitativo(nota))
