# Buscando valor com base na chave
dic_pernambuco = {"Sport": 41, "Santa Cruz": 29, "Náutico": 21}
qnt_titulos = dic_pernambuco.get("Sport")

print(qnt_titulos)
print("O Sport tem", qnt_titulos, "títulos")