# Solicita ao usuário a operação matemática desejada
operacao = input(
"""Por favor, digite a operação matemática que gostaria de completar:
+  para adição
-  para subtração
*  para multiplicação
/  para divisão
** para potenciação
%  para percentagem 
r  para raiz quadrada\n""")

# Verifica a operação escolhida pelo usuário e executa a operação correspondente
if operacao == '+':
    numero_1 = int(input('Insira o seu primeiro número: '))
    numero_2 = int(input('Insira o seu segundo número: '))  
    print('{} + {} = {}'.format(numero_1, numero_2, numero_1 + numero_2))

elif operacao == '-':
    numero_1 = int(input('Insira o seu primeiro número: '))
    numero_2 = int(input('Insira o seu segundo número: '))
    print('{} - {} = {}'.format(numero_1, numero_2, numero_1 - numero_2))

elif operacao == '*':
    numero_1 = int(input('Insira o seu primeiro número: '))
    numero_2 = int(input('Insira o seu segundo número: '))
    print('{} * {} = {}'.format(numero_1, numero_2, numero_1 * numero_2))

elif operacao == '/':
    numero_1 = int(input('Insira o seu primeiro número: '))
    numero_2 = int(input('Insira o seu segundo número: '))
    print('{} / {} = {}'.format(numero_1, numero_2, numero_1 / numero_2))

elif operacao == '**':
    numero_1 = int(input('Insira o seu primeiro número: '))
    numero_2 = int(input('Insira o seu segundo número: '))
    print('{} ** {} = {}'.format(numero_1, numero_2, numero_1 ** numero_2))

elif operacao == '%':
    numero_1 = int(input('Insira a porcentagem: '))
    numero_2 = int(input('Insira o número: '))
    print('{}% de {} = {}'.format(numero_1, numero_2, (numero_2 * numero_1) / 100))

elif operacao == 'r':
    numero = int(input('Insira o número: '))
    print('A raiz quadrada de {} é = {}'.format(numero, numero ** 0.5))

else:
    print('Não digitou um operador válido, por favor execute novamente o programa.')
