# Imprime uma linha formatada com o texto 'texto' centralizado em uma largura mínima de 10 caracteres.
# O alinhamento e a largura são controlados por especificadores fornecidos dentro das chaves {}.
# O especificador de alinhamento é fornecido como 'align' e é definido como '^', indicando alinhamento centralizado.
# O especificador de largura é fornecido como 'width' e é definido como '10', indicando uma largura mínima de 10 caracteres.
# A expressão '{:{align}{width}}' é substituída pelo texto 'texto' formatado conforme as especificações.

print('-{:{align}{width}}-'.format('texto', align='^', width='10'))
