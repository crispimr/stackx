# Tarefa 2. Estruturas condicionais e de repetição: Tabuada com entrada do usuário (FOR)
# Dev: Rafael Crispim
# Data: 5.9.2022

# Faça um programa para calcular a tabuada de qualquer número digitado pelo usuário.

n = int(input("Digite um número:"))
for i in range(1,11):
  print(i, "x", n, "=", i * n)