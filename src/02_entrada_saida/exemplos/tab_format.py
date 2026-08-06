# Define um dicionário chamado pessoas que contém informações sobre várias pessoas.
# Cada chave é um identificador (como 'chico', 'jimi', 'cid') e cada valor é outro dicionário contendo informações sobre a pessoa (nome, idade, profissão).
pessoas = {
    'chico': {'nome': 'Chico Science', 'idade': 33, 'profissão': 'Cantor'},
    'jimi': {'nome': 'Jimi Hendrix', 'idade': 27, 'profissão': 'Guitarrista'},
    'cid': {'nome': 'Cid Moreira', 'idade': 90, 'profissão': 'Jornalista'},
}

# Imprime o cabeçalho da tabela com as colunas 'Nome', 'Idade' e 'Profissão', centralizando os títulos.
print(f"{'Nome':^16} | {'Idade':^6} | {'Profissão':^15}")

# Imprime uma linha separadora para a tabela.
print(f"{'-'*16} | {'-'*6} | {'-'*15}")

# Itera sobre as chaves do dicionário pessoas.
for pessoa in pessoas:
    d = pessoas[pessoa]  # Variável que contém o dicionário de informações de uma pessoa específica.
    # Imprime as informações da pessoa formatadas na tabela.
    # {d['nome']:<16} alinha o nome da pessoa à esquerda em uma largura mínima de 16 caracteres.
    # {d['idade']:^6} centraliza a idade em uma largura mínima de 6 caracteres.
    # {d['profissão']:>15} alinha a profissão à direita em uma largura mínima de 15 caracteres.
    print(f"{d['nome']:<16} | {d['idade']:^6} | {d['profissão']:>15}")
