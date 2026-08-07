from pathlib import Path
import shutil

# ==========================================
# CONFIGURAÇÃO
# ==========================================

BASE_ORIGEM = Path(r"H:\+++Meus Arquivos\Códigos_Projetos_Python\Códigos_GitHub")
BASE_DESTINO = Path(r"H:\+++Meus Arquivos\Códigos_Projetos_Python\Códigos_GitHub\python-fundamentos")

# Adicione aqui os repositórios que deseja migrar
MAPEAMENTO = {
    # ==========================
# 10 - ARQUIVOS
# ==========================

"formatos_arquivos": "src/10_arquivos/exemplos",
"leitura_arquivo_completo": "src/10_arquivos/exemplos",
"gerador_arquivo_diretorio": "src/10_arquivos/exemplos",
"ler_salva_planilha": "src/10_arquivos/exemplos",

# ==========================
# 11 - EXCEÇÕES
# ==========================

"excecoes_erros": "src/11_excecoes/exemplos",

# ==========================
# 12 - POO
# ==========================

"python-poo": "src/12_poo/exemplos",

"orient_obj": "src/12_poo/exemplos",

"acesso_atributos_classe": "src/12_poo/exemplos",
"atributos_classe": "src/12_poo/exemplos",
"atributo_estatico": "src/12_poo/exemplos",

"metodo_estatico": "src/12_poo/exemplos",
"metodo_privado": "src/12_poo/exemplos",

"propriedade_classe": "src/12_poo/exemplos",
"propriedades_getters_setters": "src/12_poo/exemplos",
"propriedades_atributos_privados": "src/12_poo/exemplos",

"objetos_compartilhados": "src/12_poo/exemplos",
"multiplas_referencias_objeto": "src/12_poo/exemplos",

"gerenciando_propriedades": "src/12_poo/exemplos",

"heranca": "src/12_poo/exemplos",
"heranca_multilpla": "src/12_poo/exemplos",

# ==========================
# 13 - MÓDULOS
# ==========================

"importacao_modulo": "src/13_modulos/exemplos",
"importacao_metodos": "src/13_modulos/exemplos",

# ==========================
# 14 - DATAS
# ==========================

"tempo_datas": "src/14_datas_horas/exemplos",
"tempo_execucao": "src/14_datas_horas/exemplos",
"tempo_transcorrido": "src/14_datas_horas/exemplos",
"verificacao_data": "src/14_datas_horas/exemplos",
"feriados": "src/14_datas_horas/exemplos",

# ==========================
# 15 - REGEX
# ==========================

"regex": "src/15_regex/exemplos",

# ==========================
# 16 - MÓDULOS E BIBLIOTECAS
# ==========================

"aleatorio": "src/16_modulos_bibliotecas/exemplos",
"choice_choices": "src/16_modulos_bibliotecas/exemplos",
"enumerate": "src/16_modulos_bibliotecas/exemplos",
"sistema_operacional": "src/16_modulos_bibliotecas/exemplos",
"ip_rede": "src/16_modulos_bibliotecas/exemplos",

}

# ==========================================
# NÃO ALTERE DAQUI PARA BAIXO
# ==========================================

for pasta_origem, pasta_destino in MAPEAMENTO.items():

    origem = BASE_ORIGEM / pasta_origem
    destino = BASE_DESTINO / pasta_destino

    if not origem.exists():
        print(f"❌ Não encontrado: {origem}")
        continue

    destino.mkdir(parents=True, exist_ok=True)

    arquivos = list(origem.glob("*.py"))

    if not arquivos:
        print(f"⚠ Nenhum .py em {origem.name}")
        continue

    for arquivo in arquivos:

        destino_arquivo = destino / arquivo.name

        shutil.copy2(arquivo, destino_arquivo)

        print(f"✔ {arquivo.name}")
        print(f"   {origem.name}")
        print(f"   → {destino}")
        print()