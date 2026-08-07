# Dicionário contendo os nomes dos estudantes como chaves e uma lista de suas respectivas notas como valores
notas = {
    'João': [8.0, 9.0, 10.0], 
    'Maria': [9.0, 7.0, 6.0], 
    'José': [3.4, 7.0, 8.0], 
    'Cláudia': [5.5, 6.6, 8.0], 
    'Ana': [6.0, 10.0, 9.5], 
    'Joaquim': [5.5, 7.5, 9.0], 
    'Júlia': [6.0, 8.0, 7.0], 
    'Pedro': [3.0, 4.0, 6.0]
}

# Bloco try-except-else para tratar possíveis exceções ao buscar notas de um estudante
try:
    # Solicita ao usuário que digite o nome de um estudante
    nome = input("Digite o nome do(a) estudante: ")
    # Busca as notas do estudante no dicionário 'notas'
    resultado = notas[nome]
# Captura a exceção KeyError (quando a chave não é encontrada no dicionário) e imprime uma mensagem específica
except KeyError:
    print("Estudante não matriculado(a) na turma")
# Executa se nenhuma exceção foi lançada no bloco try
else:
    # Imprime as notas do estudante encontrado
    print(resultado)
