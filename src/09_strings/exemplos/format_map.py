# Similar ao format(), mas usa um mapeamento para substituir as chaves.
ponto = {'x': 4, 'y': -5}
print("{x}, {y}".format_map(ponto))  # Saída: '4, -5'
