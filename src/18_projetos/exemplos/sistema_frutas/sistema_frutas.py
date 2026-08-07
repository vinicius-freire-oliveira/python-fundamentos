# coding: utf-8

# Lista de frutas disponíveis
frutas = ['Banana', 'Maçã', 'Pera', 'Uva', 'Melancia', 'Jamelão']

# Solicita ao usuário a fruta que deseja consultar
fruta_pedida = input('Qual é a fruta que deseja consultar? ')

# Verifica se a fruta pedida está na lista de frutas disponíveis
if(fruta_pedida in frutas):
    # Se a fruta está disponível, imprime uma mensagem confirmando
    print ('Sim, temos a fruta.')
else:
    # Se a fruta não está disponível, imprime uma mensagem informando
    print ('Não temos a fruta.')
