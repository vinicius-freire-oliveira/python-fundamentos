# Imprime o cabeçalho da tabela com três colunas ('Esquerda', 'Centro', 'Direita').
# '{0:=<8}' formata o primeiro valor ('Esquerda') para alinhamento à esquerda e preenchimento com '=' para atingir uma largura mínima de 8 caracteres.
# '{1:-^8}' formata o segundo valor ('Centro') para alinhamento centralizado e preenchimento com '-' para atingir uma largura mínima de 8 caracteres.
# '{2:.>8}' formata o terceiro valor ('Direita') para alinhamento à direita e preenchimento com '.' para atingir uma largura mínima de 8 caracteres.

print('{0:=<8} | {1:-^8} | {2:.>8}'.format('Esquerda', 'Centro', 'Direita'))

# Imprime uma linha da tabela com os valores 11, 22 e 33.
# Os valores são alinhados de acordo com as especificações de formatação.
# '{0:=<8}' garante que o primeiro valor ('11') seja alinhado à esquerda e preenchido com '=' para atingir uma largura mínima de 8 caracteres.
# '{1:-^8}' centraliza o segundo valor ('22') e preenche com '-' para atingir uma largura mínima de 8 caracteres.
# '{2:.>8}' alinha o terceiro valor ('33') à direita e preenche com '.' para atingir uma largura mínima de 8 caracteres.
print('{0:=<8} | {1:-^8} | {2:.>8}'.format(11, 22, 33))
