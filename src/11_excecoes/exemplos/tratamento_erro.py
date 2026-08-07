try:
    # Solicita ao usuário dois números e converte-os para float
    numero_1 = float(input())
    numero_2 = float(input())
    
    # Realiza a divisão dos números
    divisao = numero_1 / numero_2

except Exception as e:
    # Se ocorrer um erro durante a execução do bloco try, captura a exceção
    # Imprime o tipo de exceção e uma mensagem de erro específica
    print(type(e), f'Erro: {e}')

