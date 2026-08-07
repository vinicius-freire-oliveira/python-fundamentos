# Inverte a ordem dos carateres
# Define a função 'reverso' que recebe um parâmetro 'n'
def reverso(n):
    # Retorna a representação reversa de 'n' como uma string
    return str(n[::-1])

# Solicita ao usuário que digite um número ou uma palavra e remove espaços extras
n = str(input('Digite um número ou palavra: ')).strip()

# Chama a função 'reverso' com o valor digitado pelo usuário e imprime o resultado
print(f'Reverso: {reverso(n)}')
