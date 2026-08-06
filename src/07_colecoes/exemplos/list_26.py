# Crie um sistema que o usuário armazene 3 notas de um aluno e 
# no final é mostrado qual é a média que esse aluno teve e 
# se ele alcançar a média 7 está aprovado caso o contrário 
# está reprovado, utilizando listas:
listas_notas = []
nota1 = float(input("Digite aqui a primeira nota: "))
nota2 = float(input("Digite aqui a segunda nota: "))
nota3 = float(input("Digite aqui a terceira nota: "))

listas_notas.append(nota1)
listas_notas.append(nota2)
listas_notas.append(nota3)

media = (nota1 + nota2 + nota3) / 3

print("A média do aluno é: ", media)

if(media >= 7):
    print("O aluno está aprovado!")
else:
    print("O aluno está reprovado!")