"""Requisitos: 
- RG = 7 dígitos com a formatação X.XXX.XXX, com o órgão emissor: SSD/PE 
- CPF = 11 dígitos com a formatação XXX.XXX.XXX-XX
- CNPJ =  14 dígitos com a formatação XX.XXX.XXX/0001-XX:
    * A inscrição são os primeiros 8 dígitos, a parte que representa se é matriz ou filial (0001 – matriz, ou 0002 – filial), e finalmente dois dígitos verificadores. composto de 12 dígitos. Os dois primeiros dígitos informam a Circunscrição Militar da região, os três seguintes são relativos à Junta de Serviço Militar de cada cidade. Os seis dígitos seguintes formam um que segue em sequência, e o último é o dígito verificador. 
- CTPS = formatação é XXXXXXX/XXXX
- PIS = formatação XXX.XXXXX.XX-X
- Título de eleitor = 12 dígitos, três grupos com quatro dígitos com a formatação = XXXX XXXX XXXX:
    * Zona com três dígitos
    * seção com quatro dígitos """

import random

class GeradorDocumentos:
    @staticmethod
    def gerar_cpf():
        cpf_base = [str(random.randint(0, 9)) for _ in range(10)]
        cpf_parcial = cpf_base + [calcular_digito_cpf(cpf_base)]
        cpf = ''.join(cpf_parcial)
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

    @staticmethod
    def gerar_cnpj():
        cnpj_base = [str(random.randint(0, 9)) for _ in range(12)]
        cnpj = ''.join(cnpj_base)
        return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/0001-{calcular_digito_cnpj(cnpj_base)}"

    @staticmethod
    def gerar_ctps():
        ctps_base = [str(random.randint(0, 9)) for _ in range(11)]
        ctps = ''.join(ctps_base)
        return f"{ctps[:7]}/{ctps[7:]}"

    @staticmethod
    def gerar_pis():
        pis_base = [str(random.randint(0, 9)) for _ in range(10)]
        pis = ''.join(pis_base)
        return f"{pis[:3]}.{pis[3:8]}.{pis[8:10]}-{calcular_digito_pis(pis_base)}"

    @staticmethod
    def gerar_rg():
        rg_base = [str(random.randint(0, 9)) for _ in range(7)]
        rg = ''.join(rg_base)
        return f"{rg[:1]}.{rg[1:4]}.{rg[4:7]} - SSD/PE"

    @staticmethod
    def gerar_titulo_eleitor():
        titulo_base = [str(random.randint(0, 9)) for _ in range(12)]
        titulo = ''.join(titulo_base)
        zona = random.randint(1, 999)
        secao = random.randint(1, 9999)
        return f"{titulo[:4]} {titulo[4:8]} {titulo[8:]} Zona: {zona} Seção: {secao}"

    @staticmethod
    def gerar_reservista():
        reservista_base = [str(random.randint(0, 9)) for _ in range(12)]
        reservista_parcial = reservista_base + [calcular_digito_reservista(reservista_base)]
        reservista = ''.join(reservista_parcial)
        return f"{reservista[:2]}-{reservista[2:5]}-{reservista[5:11]}-{reservista[11]}"

# Função para calcular o dígito verificador do CPF
def calcular_digito_cpf(cpf_base):
    soma = sum((len(cpf_base) + 1 - i) * int(cpf_base[i]) for i in range(len(cpf_base)))
    digito = 11 - (soma % 11)
    return str(digito) if digito < 10 else '0'

# Função para calcular o dígito verificador do PIS
def calcular_digito_pis(pis_base):
    pesos = [3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = sum(p * int(pis_base[i]) for i, p in enumerate(pesos))
    resto = soma % 11
    return '0' if resto < 2 else str(11 - resto)

# Função para calcular os dois últimos dígitos verificadores do CNPJ
def calcular_digito_cnpj(cnpj_base):
    def calcular_digito(digitos):
        pesos = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        soma = sum(p * int(digitos[i]) for i, p in enumerate(pesos))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    primeiro_digito = calcular_digito(cnpj_base)
    cnpj_base.append(str(primeiro_digito))
    segundo_digito = calcular_digito(cnpj_base)
    return f"{primeiro_digito}{segundo_digito}"


# Função para calcular o dígito verificador do reservista
def calcular_digito_reservista(reservista_base):
    soma = sum((len(reservista_base) + 1 - i) * int(reservista_base[i]) for i in range(len(reservista_base)))
    digito = 11 - (soma % 11)
    return str(digito) if digito < 10 else '0'

# Simulação de geração de documentos
def simular_documentos():
    print("Simulação de Documentos\n")
    print("CPF:", GeradorDocumentos.gerar_cpf())
    print("CNPJ:", GeradorDocumentos.gerar_cnpj())
    print("CTPS:", GeradorDocumentos.gerar_ctps())
    print("PIS:", GeradorDocumentos.gerar_pis())
    print("RG:", GeradorDocumentos.gerar_rg())
    print("Título de Eleitor:", GeradorDocumentos.gerar_titulo_eleitor())
    print("Certificado de Reservista:", GeradorDocumentos.gerar_reservista())

# Executar a simulação
simular_documentos()
