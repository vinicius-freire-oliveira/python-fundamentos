# Solicita ao usuário que insira a palavra secreta e a converte para minúsculas
# e remove espaços em branco extras
palavra = input("Digite a palavra secreta:").lower().strip()

# Limpa a tela imprimindo 100 linhas vazias
for x in range(100):
    print()

# Inicializa listas para armazenar letras digitadas, acertos e contagem de erros
digitadas = []
acertos = []
erros = 0

# Loop principal do jogo
while True:
    senha = ""
    # Monta a senha oculta substituindo letras não acertadas por pontos
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(senha)
    
    # Verifica se o jogador acertou a palavra secreta
    if senha == palavra:
        print("Você acertou!")
        break
    
    # Solicita uma letra ao jogador
    tentativa = input("\nDigite uma letra:").lower().strip()
    
    # Verifica se a letra já foi digitada anteriormente
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas += tentativa
        # Verifica se a letra está na palavra secreta
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")

    # Imprime o desenho da forca de acordo com o número de erros
    print("X==:==\nX  :   ")
    print("X  O   " if erros >= 1 else "X")

    linha2 = ""
    if erros == 2:
        linha2 = r"  |   "
    elif erros == 3:
        linha2 = r" \|   "
    elif erros >= 4:
        linha2 = r" \|/ "
    print(f"X{linha2}")
    
    linha3 = ""
    if erros == 5:
        linha3 += r" /     "
    elif erros >= 6:
        linha3 += r" / \ "
    print(f"X{linha3}")
    
    print("X\n===========")
    
    # Verifica se o jogador foi enforcado (atingiu o limite de erros)
    if erros == 6:
        print("Enforcado!")
        print(f"A palavra secreta era: {palavra}")
        break
