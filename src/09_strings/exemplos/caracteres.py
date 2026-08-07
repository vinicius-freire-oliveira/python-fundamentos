# Inicializa uma variável 'total' para contar o número de caracteres na palavra
total = 0

# Define a palavra alvo
palavra = "data analytics"

# Inicializa a variável 'acabou' como False para indicar que ainda não acabou de percorrer a palavra
acabou = False

# Loop while para percorrer cada caractere da palavra
while (not acabou):
    # Atualiza 'acabou' como True quando 'total' é igual ao comprimento da palavra
    acabou = (total == len(palavra))
    # Incrementa 'total' para contar o número de caracteres percorridos
    total = total + 1

# Como a condição de saída do loop é quando 'total' é igual ao comprimento da palavra, é necessário subtrair 1 do 'total' final
print(total - 1)

