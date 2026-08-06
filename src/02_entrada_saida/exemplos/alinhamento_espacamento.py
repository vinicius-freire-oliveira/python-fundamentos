# Imprime o cabeçalho da tabela com formatação de colunas fixas para 'Nome' e 'Idade'.
# O número antes do ':' indica a largura mínima do campo e o número depois do ':' indica a precisão.
# Portanto, '{0:16}' significa que o campo tem uma largura mínima de 16 caracteres.
# '| {1:5}' significa que o segundo campo tem uma largura mínima de 5 caracteres e será alinhado à direita.

print('{0:16} | {1:5}'.format('Nome', 'Idade'))

# Imprime uma linha da tabela com os valores 'Mike Tyson' e '33'.
# Os valores são inseridos nas posições indicadas pelos índices {0} e {1} na string de formatação.
# O primeiro valor é formatado para ter uma largura mínima de 16 caracteres e o segundo de 5 caracteres.
print('{0:16} | {1:5}'.format('Mike Tyson', 33))

# Imprime outra linha da tabela com os valores 'Ivo Pitanguy' e '64'.
# Da mesma forma, os valores são formatados de acordo com a largura mínima especificada.
print('{0:16} | {1:5}'.format('Ivo Pitanguy', 64))

# Imprime mais uma linha da tabela com os valores 'Jesse Owens' e '69'.
# '69' está em aspas simples para indicar que é uma string, não um número.
# A formatação garante que seja exibido na largura mínima de 5 caracteres.
print('{0:16} | {1:5}'.format('Jesse Owens', '69'))

# valores numéricos se alinharam à direita
# strings se alinharam à esquerda