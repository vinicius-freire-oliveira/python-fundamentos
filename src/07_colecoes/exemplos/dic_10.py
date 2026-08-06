# Mesclar dois dicionários
dic_pernambuco = {"Sport": 41, "Santa Cruz": 29, "Náutico": 21}
dic_paulista = {"Corinthians": 29, "Santos": 22, "Palmeiras": 22}

dic_pernambuco.update(dic_paulista)

print(dic_pernambuco)