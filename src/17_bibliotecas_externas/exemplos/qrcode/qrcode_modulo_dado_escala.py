import segno  # Importa o módulo segno, que é usado para criar códigos QR

# Cria um código QR de tamanho micro com o texto 'Rain' e configura o nível de correção de erro como 'q' (error='q')
micro_qrcode = segno.make('Módulo, dado, escala', error='q')

# Salva o código QR em um arquivo PNG com o nome 'rain.png', configurando a cor dos módulos escuros como 'darkblue' e a cor dos dados escuros como 'steelblue', e escala do código QR como 5
micro_qrcode.save('modulo_dado_escala.png', dark='darkblue', data_dark='steelblue', scale=10)
