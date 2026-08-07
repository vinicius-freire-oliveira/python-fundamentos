import segno  # Importa o módulo segno, que é usado para criar códigos QR

# Cria um código QR com o texto "Green ave, Kingston"
qrcode = segno.make("Dark, light, scale")

# Salva o código QR em um arquivo PNG, definindo a cor dos módulos escuros como 'darkred', a cor dos módulos claros como 'lightblue' e a escala do código QR como 10
qrcode.save('escuro_claro_escala.png', dark='darkred', light='lightblue', scale=10)
