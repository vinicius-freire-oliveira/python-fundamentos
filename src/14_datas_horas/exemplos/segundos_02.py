dias = int(input("Dias:"))
horas = int(input("Horas:"))
minutos = int(input("Minutos:"))
segundos = int(input("Segundos:"))
# Um minuto tem 60 segundos
# Uma hora tem 3600 (60 * 60) segundos0
# Um dia tem 24 horas, logo 24 * 3600 segundos = 86400 segundos
total_em_segundos = dias * 24 * 3600 + horas * 3600 + minutos * 60 + segundos

print("Convertido em segundos é igual a %d segundos." % total_em_segundos)