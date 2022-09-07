# Tarefa 8. Número maior (IF)
# Dev: Rafael Crispim
# Data: 5.9.2022

# Escreva um programa para ler 2 valores (considere que não serão informados valores iguais)
# e escrever o maior deles.

a = int(input("Digite o primeiro valor:"))
b = int(input("Digite o segundo valor:"))
if a == b:
  b = int(input("Digite outro valor para b:"))
if a > b:
  print("O maior valor é a:", a)
else:
  print("O maior valor é b:", b)