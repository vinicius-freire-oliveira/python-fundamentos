import pandas as pd

# URL da base de dados CSV
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/desafios/alunos.csv'

# Carrega os dados do CSV na variável 'dados'
dados = pd.read_csv(url)

# Imprime o DataFrame completo
print(dados)

# Imprime as primeiras 7 linhas do DataFrame
print(dados.head(7))

# Imprime as últimas linhas do DataFrame
print(dados.tail())

# Imprime as dimensões do DataFrame (número de linhas e colunas)
print(dados.shape)

# Imprime os nomes das colunas do DataFrame
print(dados.columns)

# Imprime a coluna 'Notas'
print(dados['Notas'])

# Imprime as colunas 'Nome' e 'Aprovado'
print(dados[['Nome', 'Aprovado']])

# Imprime os tipos de dados de cada coluna
print(dados.dtypes)

# Imprime estatísticas descritivas do DataFrame
print(dados.describe())

# Imprime a contagem de valores nulos em cada coluna
print(dados.isnull().sum())

# Preenche os valores nulos com 0
dados = dados.fillna(0)

# Imprime o DataFrame após preencher os valores nulos
print(dados)

# Verifica novamente a contagem de valores nulos para confirmar que foram preenchidos
print(dados.isnull().sum())

# Seleciona e imprime as linhas onde o nome é 'Alice' ou 'Carlos'
print(dados.query('Nome == "Alice" | Nome == "Carlos"'))

# Imprime os índices das linhas onde o nome é 'Alice' ou 'Carlos'
print(dados.query('Nome == "Alice" | Nome == "Carlos"').index)

# Armazena os índices das linhas onde o nome é 'Alice' ou 'Carlos' em uma variável
alunos_a_remover = dados.query('Nome == "Alice" | Nome == "Carlos"').index

# Remove as linhas correspondentes aos índices armazenados
dados.drop(alunos_a_remover, axis=0, inplace=True)

# Verifica se as linhas onde o nome é 'Alice' ou 'Carlos' foram removidas
print(dados.query('Nome == "Alice" | Nome == "Carlos"'))

# Verifica se os alunos foram aprovados
print(dados['Aprovado'] == True)

# Seleciona e imprime os alunos aprovados
selecao = dados['Aprovado'] == True
print(dados[selecao])

# Armazena os alunos aprovados em uma nova variável
alunos_aprovados = dados[selecao]

# Salva os dados dos alunos aprovados em um novo arquivo CSV
alunos_aprovados.to_csv('alunos_aprovados.csv', index=False)

# Lê e imprime os dados do novo arquivo CSV
print(pd.read_csv('alunos_aprovados.csv'))

# Imprime o DataFrame dos alunos aprovados
print(alunos_aprovados)

# Substitui a nota 7.0 por 8.0 e imprime o resultado
print(alunos_aprovados.replace(7.0, 8.0))

# Atualiza o DataFrame substituindo 7.0 por 8.0 e imprime o resultado
alunos_aprovados = alunos_aprovados.replace(7.0, 8.0)
print(alunos_aprovados)

# Adiciona uma nova coluna 'Pontos_extras' aplicando uma função lambda para calcular 40% da nota original
dados['Pontos_extras'] = dados['Notas'].apply(lambda x: x * 0.4)
print(dados)

# Adiciona uma nova coluna 'Notas_finais' somando 'Notas' e 'Pontos_extras'
dados['Notas_finais'] = dados['Notas'] + dados['Pontos_extras']
print(dados)

# Adiciona uma nova coluna 'Aprovado_final' que indica se o aluno foi aprovado considerando 'Notas_finais'
dados['Aprovado_final'] = dados['Notas_finais'].apply(lambda x: True if x >= 6 else False)
print(dados)

# Seleciona e imprime os alunos que não foram aprovados inicialmente mas foram aprovados após a adição dos pontos extras
print(dados.query('Aprovado == False & Aprovado_final == True'))

# Cria uma seleção para alunos que não foram aprovados inicialmente mas foram aprovados após a adição dos pontos extras
selecao = (dados['Aprovado'] == False) & (dados['Aprovado_final'] == True)

# Imprime os alunos que atendem à seleção
print(dados[selecao])
