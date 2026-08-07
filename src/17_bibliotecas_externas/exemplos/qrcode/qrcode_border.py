import segno  # Importa o módulo segno, que é usado para criar códigos QR

# Cria um código QR com o texto 'Beatles'
qrcode = segno.make('Beatles')

# Salva o código QR em um arquivo PNG com o nome 'vampire-blues.png', configurando uma borda de tamanho 5
qrcode.save('border.png', border=4, scale=10)
