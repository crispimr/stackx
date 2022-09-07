# Tarefa 2. Idade e peso (IF)
# Dev: Rafael Crispim
# Data: 4.9.2022

# Faça um programa que receba a idade e o peso de uma pessoa.
# De acordo com a tabela a seguir, verifique e mostre em qual grupo de risco
# essa pessoa se encaixa.
# IDADE           ATÉ 60KG  ENTRE 60 E 90KG ACIMA DE 90KG
# Menores que 20  9         8               7
# De 20 a 50      6         5               4
# Maiores que 50  3         2               1

Idade = int(input("Digite a sua idade: "))
Peso = float(input("Digite o seu peso: "))

if Idade < 20 and Peso <= 60:
  print("Com", Idade, "anos e o peso de", Peso, "Kilos, você está no grau de risco 9")
elif Idade < 20 and Peso > 60 and Peso <= 90:
  print("Com", Idade, "anos e o peso de", Peso, "Kilos, você está no grau de risco 8")
elif Idade < 20 and Peso > 90:
  print("Com", Idade, "anos e o peso de", Peso, "Kilos, você está no grau de risco 7")
elif Idade >= 20 and Idade <= 50 and Peso <= 60:
  print("Com", Idade, "anos e o peso de", Peso, "Kilos, você está no grau de risco 6")
elif Idade >= 20 and Idade <= 50 and Peso > 60 and Peso <= 90:
  print("Com", Idade, "anos e o peso de", Peso, "Kilos, você está no grau de risco 5")
elif Idade >= 20 and Idade <= 50 and Peso > 90:
  print("Com", Idade, "anos e o peso de", Peso, "Kilos, você está no grau de risco 4")
elif Idade > 50 and Peso <= 60:
  print("Com", Idade, "anos e o peso de", Peso, "Kilos, você está no grau de risco 3")
elif Idade > 50 and Peso > 60 and Peso <= 90:
  print("Com", Idade, "anos e o peso de", Peso, "Kilos, você está no grau de risco 2")
elif Idade > 50 and Peso > 90:
  print("Com", Idade, "anos e o peso de", Peso, "Kilos, você está no grau de risco 1")