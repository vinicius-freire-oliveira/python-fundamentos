# Solicitação do valor inicial do investimento
vi = float(input('Valor inicial: '))

# Solicitação da rentabilidade mensal em porcentagem
i = float(input('Rentabilidade mensal (%): '))

# Transformação da taxa de rentabilidade de porcentagem para valor decimal
i = i / 100

# Solicitação do período de investimento em meses
m = int(input('Número de meses de investimento: '))

# Cálculo do valor final do investimento
vf = vi * (1 + i) ** m

# Exibição do valor final do investimento
print('Valor após', m, 'meses: R$ {:.2f}'.format(vf))




