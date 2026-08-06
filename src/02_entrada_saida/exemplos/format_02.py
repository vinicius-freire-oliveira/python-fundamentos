linguagem_preferida = "Python"

# Imprime uma frase usando a formatação de string antiga com o operador de formatação '%'.
# O '%s' indica que será substituído por uma string e o valor a ser substituído é 'linguagem_preferida'.
print("Eu amo %s" %(linguagem_preferida))

# Imprime uma frase usando a formatação de string antiga.
# O '%d' indica que será substituído por um número inteiro e o valor a ser substituído é '19'.
print("Eu tenho %d" %(19))

# Imprime uma frase usando a formatação de string antiga.
# O '%02d' indica que será substituído por um número inteiro com pelo menos 2 dígitos, preenchendo com zeros à esquerda, e o valor a ser substituído é '9'.
print("Eu tenho %02d anos de idade" %(9))

# Imprime uma frase usando a formatação de string antiga.
# O '%03d' indica que será substituído por um número inteiro com pelo menos 3 dígitos, preenchendo com zeros à esquerda, e o valor a ser substituído é '19'.
# O '%2.5f' indica que será substituído por um número de ponto flutuante com pelo menos 2 dígitos à esquerda e 5 à direita, e o valor a ser substituído é '100'.
print("Eu tenho %03d anos de idade e %2.5f na poupança" %(19,100))
