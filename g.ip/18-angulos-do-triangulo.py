# Tarefa 18. Ângulos do triângulo (IF)
# Dev: Rafael Crispim
# Data: 5.9.2022

# Escreva um programa que leia o valor de 3 ângulos de um triângulo e escreva se o triângulo
# é Acutângulo, Retângulo ou Obtusângulo.
# Sendo que:
# Triângulo Retângulo: possui um ângulo reto. (igual a 90º)
# Triângulo Obtusângulo: possui um ângulo obtuso. (maior que90º)
# TriânguloAcutângulo: possui três ângulos agudos. (menor que 90º

a = int(input("Digite o valor do ângulo 1:"))
b = int(input("Digite o valor do ângulo 2:"))
c = int(input("Digite o valor do ângulo 3:"))
if a == 90 or b == 90 or c == 90:
  print("Triângulo Retângulo")
elif a > 90 or b > 90 or c > 90:
  print("Triângulo Obtusângulo")
else:
  print("Triângulo Acutângulo")