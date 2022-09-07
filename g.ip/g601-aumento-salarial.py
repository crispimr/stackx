# Tarefa 1. Estruturas condicionais e de repetição: Aumento salarial (FOR)
# Dev: Rafael Crispim
# Data: 5.9.2022

# Um funcionário de uma empresa recebe, anualmente, aumento salarial. Sabe-se que:
# a) esse funcionário foi contratado em 2000, com salário inicial de R$1.000,00;
# b) Em 2001, ele recebeu aumento de 1,5%, sobre o seu salário inicial;
# c) A partir de 2002 (inclusive), os aumentos salariais sempre corresponderam ao
# dobro do percentual do ano anterior.
# Faça um programa que determine o salário desse funcionário dos anos de 2000 à 2017.
# Apresente todos os valores.

SalarioInicial = 1000
PercAumento = 0.015
Salario = SalarioInicial
for i in range (2000, 2018):
  if i == 2001:
    Salario = Salario * 1.015
  elif i > 2001:
    Salario = Salario * (1 + 0.015 * 2)
    print("Ano:", i, "Salario:", Salario)
  else:
    print("Ano:", i, "Salário:", Salario)