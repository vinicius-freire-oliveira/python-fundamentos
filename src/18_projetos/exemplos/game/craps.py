""" Regras do Craps Tradicional
No jogo de Craps tradicional:
1 - O jogador lança dois dados.
2 - Na primeira jogada:
• Se a soma dos dados for 7 ou 11, o jogador ganha.
• Se a soma for 2, 3 ou 12 (conhecido como "craps"), o jogador perde.
• Qualquer outro resultado torna-se o "ponto" do jogador.
3 - Se um ponto é estabelecido (qualquer número diferente de 7, 11, 2, 3 ou 12):
• O jogador continua lançando os dados até obter o mesmo ponto novamente (ganhando) ou um 7 (perdendo). """

# Importa a função randint do módulo random
from random import randint

# Define uma variável global k inicializada como 0
k = 0

# Define a função craps
def craps():
    # Gera um número aleatório entre 2 e 13 e armazena em k
    k = randint(2, 13)
    
    # Verifica se k é 7 ou 11
    if k == 7 or k == 11:
        print('Você é um natural!! Parabéns você ganhou!!', k)
    
    # Verifica se k é 2, 3 ou 12
    elif k == 2 or k == 3 or k == 12:
        print('Craps!!! Lamento você perdeu!', k)
    
    # Caso k não seja nenhum dos valores acima
    else:
        # Imprime uma mensagem e o número k
        print('Esse é o seu número vamos jogar!! Número:', k)
        print('Digite D para jogar o dado: ')
        
        # Inicializa a variável z como 0
        z = 0
        
        # Loop enquanto k for diferente de z
        while k != z:
            print('Digite D para jogar o dado:')
            
            # Solicita ao usuário para digitar 'D' para jogar o dado
            s = input()
            
            # Verifica se o usuário digitou 'D'
            if s == 'D':
                # Gera um número aleatório entre 2 e 13 e armazena em z
                z = randint(2, 13)
                
                # Imprime o número gerado
                print('Seu número foi: ', z)
                
                # Verifica se z é igual a 7
                if z == 7:
                    print('Infelizmente você Perdeu!!!')
                    break
        
        # Verifica se z é diferente de 7
        if z != 7:
            print('Parabéns você Ganhou!!!')

# Chama a função craps para iniciar o jogo
craps()
