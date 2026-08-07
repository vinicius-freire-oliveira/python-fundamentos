from datetime import datetime, timedelta

# Função para calcular a data da Páscoa
def calcular_pascoa(ano):
    a = ano % 19
    b = ano // 100
    c = ano % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    mes_pascoa = (h + l - 7 * m + 114) // 31
    dia_pascoa = ((h + l - 7 * m + 114) % 31) + 1
    return datetime(ano, mes_pascoa, dia_pascoa)

# Função para calcular o São João (24 de junho)
def calcular_sao_joao(ano):
    sao_joao = datetime(ano, 6, 24)
    return sao_joao

# Função para calcular o Dia dos Namorados (12 de junho)
def calcular_dia_dos_namorados(ano):
    dia_dos_namorados = datetime(ano, 6, 12)
    return dia_dos_namorados

# Função para calcular o Dia das Crianças (12 de outubro)
def calcular_dia_das_criancas(ano):
    dia_das_criancas = datetime(ano, 10, 12)
    return dia_das_criancas

# Função para calcular o Dia do Professor (15 de outubro)
def calcular_dia_do_professor(ano):
    dia_do_professor = datetime(ano, 10, 15)
    return dia_do_professor

# Função para calcular o Dia da Consciência Negra (20 de novembro)
def calcular_dia_da_consciencia_negra(ano):
    dia_da_consciencia_negra = datetime(ano, 11, 20)
    return dia_da_consciencia_negra

# Função para calcular o Dia das Mães (segundo domingo de maio)
def calcular_dia_das_maes(ano):
    primeiro_de_maio = datetime(ano, 5, 1)
    dia_da_semana = primeiro_de_maio.weekday()
    if dia_da_semana == 6:
        return primeiro_de_maio + timedelta(days=7)
    return primeiro_de_maio + timedelta(days=(6 - dia_da_semana) + 7)

# Função para calcular o Dia dos Pais (segundo domingo de agosto)
def calcular_dia_dos_pais(ano):
    primeiro_de_agosto = datetime(ano, 8, 1)
    dia_da_semana = primeiro_de_agosto.weekday()
    if dia_da_semana == 6:
        return primeiro_de_agosto + timedelta(days=7)
    return primeiro_de_agosto + timedelta(days=(6 - dia_da_semana) + 7)

# Função para traduzir o nome do dia da semana para o português
def traduzir_dia_da_semana(data):
    dias_da_semana = {
        0: "Segunda-feira",
        1: "Terça-feira",
        2: "Quarta-feira",
        3: "Quinta-feira",
        4: "Sexta-feira",
        5: "Sábado",
        6: "Domingo"
    }
    return dias_da_semana[data.weekday()]

# Função para listar os feriados
def listar_feriados(ano):
    pascoa = calcular_pascoa(ano)
    sao_joao = calcular_sao_joao(ano)
    dia_dos_namorados = calcular_dia_dos_namorados(ano)
    dia_das_criancas = calcular_dia_das_criancas(ano)
    dia_do_professor = calcular_dia_do_professor(ano)
    dia_da_consciencia_negra = calcular_dia_da_consciencia_negra(ano)
    dia_das_maes = calcular_dia_das_maes(ano)
    dia_dos_pais = calcular_dia_dos_pais(ano)

    feriados = {
        "Ano Novo": datetime(ano, 1, 1),
        "Carnaval": pascoa - timedelta(days=47),
        "Sexta-feira Santa": pascoa - timedelta(days=2),
        "Páscoa": pascoa,
        "Tiradentes": datetime(ano, 4, 21),
        "Dia do Trabalhador": datetime(ano, 5, 1),
        "Corpus Christi": pascoa + timedelta(days=60),
        "Independência do Brasil": datetime(ano, 9, 7),
        "Nossa Senhora Aparecida": datetime(ano, 10, 12),
        "Dia das Mães": dia_das_maes,
        "Dia dos Pais": dia_dos_pais,
        "Finados": datetime(ano, 11, 2),
        "Proclamação da República": datetime(ano, 11, 15),
        "Natal": datetime(ano, 12, 25),
        "São João": sao_joao,
        "Dia dos Namorados": dia_dos_namorados,
        "Dia das Crianças": dia_das_criancas,
        "Dia do Professor": dia_do_professor,
        "Dia da Consciência Negra": dia_da_consciencia_negra,
    }
    
    return feriados

# Solicitação do ano ao usuário
ano = int(input("Informe o ano para listar os feriados e as datas comemorativas: "))

# Listagem dos feriados
feriados_do_ano = listar_feriados(ano)

# Exibição dos feriados
print(f"Feriados do ano de {ano}:\n")
for nome, data in sorted(feriados_do_ano.items(), key=lambda x: x[1]):
    print(f"{nome}: {data.strftime('%d/%m/%Y')} ({traduzir_dia_da_semana(data)})")
