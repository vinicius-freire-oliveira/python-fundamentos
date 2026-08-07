# Importa as bibliotecas pandas e sqlalchemy necessárias
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, inspect, text

# Cria um mecanismo de banco de dados SQLite em memória
engine = create_engine('sqlite:///:memory:')

# URL do arquivo CSV que será lido
url = 'https://raw.githubusercontent.com/alura-cursos/Pandas/main/clientes_banco.csv'

# Lê os dados do arquivo CSV a partir da URL e carrega em um DataFrame
dados = pd.read_csv(url)

# Imprime as primeiras linhas do DataFrame 'dados' para verificar a leitura
print(dados.head())

# Converte o DataFrame 'dados' em uma tabela SQL chamada 'clientes' dentro do banco de dados SQLite em memória
dados.to_sql('clientes', engine, index=False)

# Cria um objeto Inspector para inspecionar o mecanismo de banco de dados
inspector = inspect(engine)

# Imprime os nomes das tabelas presentes no banco de dados
print(inspector.get_table_names())

# Query SQL para selecionar todos os registros onde a coluna 'Categoria_de_renda' é igual a "Empregado"
query = 'SELECT * FROM clientes WHERE Categoria_de_renda = "Empregado"'

# Executa a query SQL no banco de dados e carrega os resultados em um DataFrame chamado 'empregados'
empregados = pd.read_sql(query, engine)

# Imprime o DataFrame 'empregados' com os registros filtrados
print(empregados)

# Converte o DataFrame 'empregados' em uma nova tabela SQL chamada 'empregados' no banco de dados
empregados.to_sql('empregados', con=engine, index=False)

# Imprime o conteúdo da tabela SQL 'empregados' lida do banco de dados
print(pd.read_sql_table('empregados', engine))

# Imprime apenas as colunas especificadas da tabela SQL 'empregados'
print(pd.read_sql_table('empregados', engine, columns=['ID_Cliente', 'Grau_escolaridade', 'Rendimento_anual']))

# Query SQL para selecionar todos os registros da tabela 'clientes'
query = 'SELECT * FROM clientes'

# Executa a query SQL no banco de dados e imprime o resultado
print(pd.read_sql(query, engine))

# Query SQL para deletar um registro específico da tabela 'clientes'
query = text('DELETE FROM clientes WHERE ID_Cliente=5008804')

# Conecta-se ao banco de dados e executa a query de deleção
with engine.connect() as conn:
    conn.execute(query)

# Imprime o conteúdo atualizado da tabela 'clientes' após a deleção
print(pd.read_sql_table('clientes', engine))

# Query SQL para atualizar um registro específico na tabela 'clientes'
query = text('UPDATE clientes SET Grau_escolaridade="Ensino superior" WHERE ID_Cliente=5008808')

# Conecta-se ao banco de dados e executa a query de atualização
with engine.connect() as conn:
    conn.execute(query)

# Imprime o conteúdo atualizado da tabela 'clientes' após a atualização
print(pd.read_sql_table('clientes', engine))
