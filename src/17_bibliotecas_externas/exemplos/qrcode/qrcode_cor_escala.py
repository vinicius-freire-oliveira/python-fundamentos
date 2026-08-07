import segno  # Importa o módulo segno, que é usado para criar códigos QR

# Cria um código QR contendo o endereço "Green ave, Kingston"
qrcode = segno.make('Blue QR Code')

# Salva o código QR em um arquivo PNG, configurando a cor dos módulos escuros com transparência alfa e a escala do código QR
qrcode.save('cor_escala.png', dark='#0000ffcc', scale=10)
