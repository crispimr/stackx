# Tarefa 12. 3 valores em ordem (IF)
# Dev: Rafael Crispim
# Data: 5.9.2022

# Escreva um programa para ler 3 valores inteiros (considere que não serão lidos valores iguais)
# e escrevê-los em ordem crescente.

a = int(input("Digite o primeiro valor:"))
b = int(input("Digite o segundo valor:"))
c = int(input("Digite o terceiro valor:"))
if a < b:
  if a < c:
    if b < c:
      print("a:", a, "b:", b, "c:", c)
    else:
      print("a:", a, "c:", c, "b:", b)
  else:
    print("c:", c, "a:", a, "b:", b)
else:
  if b < c:
    if a < c:
      print("b:", b, "a:", a, "c:", c)
    else:
      print("b:", b, "c:", c, "a:", a)
  else:
    print("c:", c, "b:", b, "a:", a)