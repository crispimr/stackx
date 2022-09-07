# Tarefa 13. Altura e sexo (IF)
# Dev: Rafael Crispim
# Data: 5.9.2022

# Tendo como entrada a altura e o sexo (codificado da seguinte forma: 1: feminino 2: masculino)
# de uma pessoa, construa um programa que calcule e imprima seu peso ideal, utilizando as seguintes Fórmulas:
# para homens: (72.7 * Altura) – 58
# para mulheres: (62.1 * Altura) – 44.7

Altura = float(input("Digite sua altura em metros:"))
Sexo = int(input("Digite seu sexo (1 = F, 2 = M):"))
if Sexo == 1:
  PesoIdeal = (62.1 * Altura) - 44.7
else:
  PesoIdeal = (72.7 * Altura) - 58
print("Altura:", Altura, "Sexo", Sexo, "Peso ideal:", PesoIdeal)