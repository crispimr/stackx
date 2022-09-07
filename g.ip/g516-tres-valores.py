# Tarefa 16. Três valores e o maior deles (IF)
# Dev: Rafael Crispim
# Data: 5.9.2022

# Escreva um programa para ler 3 valores inteiros e escrever o maior deles.
# Considere que o usuário não informará valores iguais.

a = int(input("Digite o primeiro valor:"))
b = int(input("Digite o segundo valor:"))
if a == b:
  b = int(input("Digite outro segundo valor:"))
c = int(input("Digite o terceiro valor:"))
if c == a or c == b:
  b = int(input("Digite outro terceiro valor:"))

if a > b and a > c:
  print("O maior valor é de a:", a)
elif b > a and b > c:
  print("O maior valor é de b:", b)
else:
  print("O maior valor é de c:", c)