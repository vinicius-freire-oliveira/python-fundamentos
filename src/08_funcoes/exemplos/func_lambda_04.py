# Nomes dos estudantes
nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]

# Função lambda que recebe duas listas e itera em cada uma concatenando seu nome e sobrenome
# na forma desejada
nome_completo = map(lambda nome, sobrenome: f'{nome.title()} {sobrenome.title()}', nomes, sobrenomes)

# Leitura do objeto mapa(iterável)
for n in nome_completo:
  print(f'Nome completo: {n}')
