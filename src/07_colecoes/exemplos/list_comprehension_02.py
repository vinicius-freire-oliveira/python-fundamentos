nomes = [('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')]
medias = [9.0, 7.3, 5.8, 6.7, 8.5]

# Gerando a lista de nomes (extraindo da tupla)
nomes = [nome[0] for nome in nomes]
print(nomes)

estudantes = list(zip(nomes, medias))
print(estudantes)

# Gerando a lista de pessoas candidatas a bolsa
candidatos = [estudante[0] for estudante in estudantes if estudante[1] >= 8.0]
print(candidatos)

