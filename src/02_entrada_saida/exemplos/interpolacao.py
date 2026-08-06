# Imprime um valor formatado como moeda com 7 espaços no total, incluindo uma casa decimal
# O valor é alinhado à direita, e há uma casa decimal
# Saída: "R$  1000.1"
print("R$ {:7.1f}".format(1000.12))

# Imprime um valor formatado como moeda com 7 espaços no total, incluindo duas casas decimais
# O valor é preenchido com zeros à esquerda, se necessário
# Saída: "R$ 0004.11"
print("R$ {:07.2f}".format(4.11))

# Define uma variável 'nome' com o valor 'Mateus'
nome = 'Mateus'

# Imprime uma mensagem formatada usando uma f-string
# O método lower() é chamado em 'nome' para converter todas as letras em minúsculas
# Saída: "Meu nome é mateus"
print(f'Meu nome é {nome.lower()}')

