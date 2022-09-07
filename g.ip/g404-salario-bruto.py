# Tarefa 4. Salário bruto (IF)
# Dev: Rafael Crispim
# Data: 4.9.2022

# aça um programa que receba o salário bruto de um funcionário e,
# usando a tabela a seguir, calcule e mostre o valor a receber.
# Sabe-se que este é composto pelo salário bruto acrescido de gratificação
# e descontado o imposto de 7% sobre o salário.

# SALÁRIO                   GRATIFICAÇÃO
# Até R$350,00              R$100,00
# R$351,00 até R$600,00     R$75,00
# R$601,00 até R$900,00     R$50,00
# Acima de R$901,00         R$35,00

salario = float(input("Digite o valor do salário: "))
if salario <= 350:
    gratificacao = 100
elif salario >= 351 and salario <= 600:
    gratificacao = 75
elif salario >= 601 and salario <= 900:
    gratificacao = 50
else:
    gratificacao = 35
print("Para o salário de R$", salario, "a gratificação é R$", gratificacao)