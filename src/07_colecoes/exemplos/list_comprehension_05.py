# Lista de valores de glicemia
glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]

# Compreensão de lista para criar uma lista de tuplas com rótulos baseados nos níveis de glicose
rotulos = [
    ('Hipoglicemia', glicose) if glicose <= 70 
    else ('Normal', glicose) if glicose < 100 
    else ('Alterada', glicose) if glicose < 125 
    else ('Diabetes', glicose) 
    for glicose in glicemia
]

# Imprime a lista de tuplas com os rótulos correspondentes aos níveis de glicemia
print(rotulos)

