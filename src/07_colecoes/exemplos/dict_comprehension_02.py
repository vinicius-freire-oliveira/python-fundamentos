# Define uma lista de meses do ano
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

# Define uma lista de despesas correspondentes a cada mês
despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]

# Cria um dicionário onde a chave é o mês e o valor é a despesa correspondente
dicionario = {meses[i]: despesa[i] for i in range(len(meses))}

# Imprime o dicionário resultante
print(dicionario)

