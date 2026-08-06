# Criar um sistema de emprestimo que se o valor do 
"""empréstimo for menor ou igual a 50% do seu salário, então o
empréstimo será aprovado, senão, se o valor do empréstimo for 
menor ou igual a 75% do salário a situação ficará em análise, senão,
informe ao cliente que o empréstimo não foi aprovado."""
# ações:
# 1 - aprovar o empréstimo 2 - situação em análise 3 - não aprovar o empréstimo
salario = float(input("Digite aqui o seu salário: "))
emprestimo = float(input("Digite o valor do empréstimo: "))

if(emprestimo <= 0.5 * salario):
    print("\nAprovado")
elif(emprestimo <= 0.75 * salario):
    print("\nAnálise")
else:
    print("\nReprovado")