from segno import helpers  # Importa a função make_wifi do módulo helpers do pacote segno

# Cria um código QR contendo informações para acesso a uma rede Wi-Fi
qrcode = helpers.make_wifi(ssid='MyWifi', password='1234567890', security='WPA')

# Obtém o designador do código QR Wi-Fi (por exemplo, '3-M' significa versão 3 do código QR, nível de correção de erro M)
qrcode.designator

# Salva o código QR em um arquivo PNG com o nome 'wifi-access.png', configurando a escala do código QR como 10
qrcode.save('wifi-access.png', scale=10)


