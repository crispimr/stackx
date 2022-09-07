# Tarefa 14. Polígono (IF)
# Dev: Rafael Crispim
# Data: 5.9.2022

# Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm).
# Calcular e imprimir o seguinte:
# Se o número de lados for igual a 3 escrever TRIÂNGULO e o valor da área
# Se o número de lados for igual a 4 escrever QUADRADO e o valor da sua área.
# Se o número de lados for igual a 5 escrever PENTÁGONO.

import math as m

n = int(input("Digite o número de lados:"))
md = float(input("Digite a medida em cm:"))
if n == 3:
  a = ((md * md) * m.sqrt(3))/4
  print("TRIÂNGULO com ", a, "cm2")
elif n == 4:
  a = md * md
  print("QUADRADO com ", a, "cm2")
elif n == 5:
  a = 5 * (md * md) / (4 * m.sqrt(5 - 2 * m.sqrt(5)))
  print("PENTÁGONO com ", a, "cm2")