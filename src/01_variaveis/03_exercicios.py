"""
Exercícios - Variáveis

Criar um dicionário contendo:
- nome
- idade
- profissão

Depois atualizar apenas a profissão.
"""


aluno = {
    "nome": "Ana",
    "idade": 25,
    "profissao": "Estudante"
}


print("Antes da alteração:")
print(aluno)


aluno["profissao"] = "Desenvolvedora Python"


print("\nDepois da alteração:")
print(aluno)