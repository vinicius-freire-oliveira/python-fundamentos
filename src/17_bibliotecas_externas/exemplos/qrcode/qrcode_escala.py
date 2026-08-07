import segno  # Importa o módulo segno, que é usado para criar códigos QR

# Cria um código QR com o texto 'Welcome'
qrcode = segno.make_qr('Scale')

# Salva o código QR em um arquivo PNG com o nome 'welcome.png', configurando a escala do código QR como 10
qrcode.save('escala.png', scale=10)
