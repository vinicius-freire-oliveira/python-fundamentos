from segno import helpers  # Importa o módulo helpers do módulo segno, que fornece funções auxiliares para criar códigos QR específicos

# Cria um código QR MeCard com informações de contato para um indivíduo
qrcode = helpers.make_mecard(name='Shittu Olumide', email='me@example.com', phone='+123456789')

# Obtém o designador do código QR MeCard (por exemplo, '3-L' significa versão 3 do código QR, nível de correção de erro L)
qrcode.designator

# Alguns parâmetros aceitam vários valores, como e-mail, telefone e URL
qrcode = helpers.make_mecard(name='Ringo Starr', 
                             email=('me@example.com', 'email@example.com'),
                             url=['http://www.example.com', 'https://example.com/~olu'])

# Salva o código QR em um arquivo PNG com o nome 'mycontact1.png' e escala de 5
qrcode.save('contatos.png', scale=5)
