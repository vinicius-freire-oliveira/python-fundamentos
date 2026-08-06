# Lista de notas do(a) estudante
notas = [6.0, 7.0, 9.0, 5.5, 8.0]

# Valor qualitativo a ser adicionado a cada nota
qualitativo = 0.5

# Aplicação de uma função lambda para atualizar as notas
# Usamos a função map para aplicar o lambda a cada elemento da lista
notas_atualizadas = map(lambda x: x + qualitativo, notas)

# A função map retorna um iterador, então convertemos para lista para visualização
notas_atualizadas = list(notas_atualizadas)

# Imprime as notas atualizadas
print(notas_atualizadas)

# Imprime a lista original de notas
print(notas)
