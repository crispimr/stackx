# Tarefa 7. Conjunto de valores (While)
# Dev: Rafael Crispim
# Data: 5.9.2022

# Faça um programa que leia um conjunto não determinado de valores e mostre o valor lido,
# seu quadrado, seu cubo e sua raiz quadrada. Finalize a entrada de dados com um valor negativo ou zero.

import math as m
Entrada = 1

while Entrada > 0:
  Entrada = int(input("Digite um valor:"))
  print("Valor:", Entrada, "Quadrado", Entrada ** 2, "Cubo:", Entrada ** 3, "Raíz:", m.sqrt(Entrada))
print("Acabou :)")