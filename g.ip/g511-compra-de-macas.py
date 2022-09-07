# Tarefa 11. Compra de maçâs (IF)
# Dev: Rafael Crispim
# Data: 5.9.2022

# As maçãs custam R$ 0,30 cada se forem compradas menos do que uma dúzia,
# e R$ 0,25 se forem compradas pelo menos doze. Escreva um programa que leia
# o número de maçãs compradas, calcule e escreva o valor total da compra.

n = int(input("Digite o número de maçãs compradas:"))
if n < 12:
  print("Para ", n, "maçã(s) o valor unitário é de R$0,30 e o valor total é de R$", n * 0.30)
else:
  print("Para ", n, "maçã(s) o valor unitário é de R$0,25 e o valor total é de R$", n * 0.25)