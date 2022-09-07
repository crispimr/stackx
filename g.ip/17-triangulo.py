# Tarefa 16. Três valores e o maior deles (IF)
# Dev: Rafael Crispim
# Data: 5.9.2022

# Escreva um programa que leia as medidas dos lados de um triângulo e escreva se ele é Equilátero,
# Isósceles ou Escaleno.
# Sendo que:
# Triângulo Equilátero: possui os 3 lados iguais.
# Triângulo Isóscele: possui 2 lados iguais.
# Triângulo Escaleno: possui 3 lados diferentes.

a = int(input("Digite a medida do lado 1:"))
b = int(input("Digite a medida do lado 2:"))
c = int(input("Digite a medida do lado 3:"))
if a == b and a == c or b == a and b == c or c == a and c == b:
  print("Equilátero")
elif a == b or a == c or b == a or b == c or c == a or c == b:
  print("Isóscele")
else:
  print("Escaleno")