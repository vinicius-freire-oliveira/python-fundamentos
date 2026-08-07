import segno  # Importa o módulo segno, que é usado para criar códigos QR

# Cria um código QR com o texto "Hello World"
price_tag = segno.make("Bem-vindo")

# Salva o código QR em um arquivo PNG com o nome "hello-world.png"
price_tag.save("msg.png", scale=10)
