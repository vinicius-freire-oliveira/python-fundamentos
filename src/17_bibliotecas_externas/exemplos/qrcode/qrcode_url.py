import segno  # Importa o módulo segno, que é usado para criar códigos QR

# Cria um código QR contendo o link para o canal do YouTube '@TheBeatles'
video = segno.make('https://www.youtube.com/@TheBeatles')

# Salva o código QR em um arquivo PNG com o nome 'Video.png', configurando a cor dos módulos escuros como "yellow", a cor dos módulos claros como "#323524" e a escala do código QR como 5
video.save('Video.png', dark="yellow", light="#323524", scale=5)
