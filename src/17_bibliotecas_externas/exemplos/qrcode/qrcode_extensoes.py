import segno  # Importa o módulo segno, que é usado para criar códigos QR

# Cria um código QR com o texto 'Beatles'
qrcode = segno.make('Beatles')

# Salva o código QR em um arquivo EPS (Encapsulated PostScript)
qrcode.save('Beatles.eps')

# Salva o código QR em um arquivo PNG (Portable Network Graphics)
qrcode.save('Beatles.png', scale=20)

# Salva o código QR em um arquivo SVG (Scalable Vector Graphics)
qrcode.save('Beatles.svg')