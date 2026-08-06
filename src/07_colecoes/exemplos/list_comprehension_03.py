# Lista de tuplas com nomes e códigos de identificação
nomes = [('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')]

# Lista de listas com notas de cada aluno
notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]

# Lista de médias de cada aluno
medias = [9.0, 7.3, 5.8, 6.7, 8.5]

# Lista de situações de cada aluno (aprovado ou reprovado)
situacao = ["Aprovado(a)" if media >= 6 else "Reprovado(a)" for media in medias]
print(situacao)

print()

# Lista completa de informações dos alunos
cadastro = [x for x in [nomes, notas, medias, situacao]]
print(cadastro)

print()

# Lista completa com cada categoria separada
lista_completa = [nomes, notas, medias, situacao]
print(lista_completa)
