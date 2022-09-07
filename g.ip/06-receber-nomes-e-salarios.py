# Tarefa 6. Receber nomes e salários (While)
# Dev: Rafael Crispim
# Data: 5.9.2022

# Faça um programa que receba o salário de um funcionário chamado Carlos.
# Sabe-se que outro funcionário, João, tem salário equivalente a um terço do salário de Carlos.
# Carlos aplicará seu salário integralmente na caderneta de poupança, que rende 2% ao mês,
# e João aplicará seu salário integralmente no fundo de renda fixa, que rende 5% ao mês.
# O programa deverá calcular e mostrar a quantidade de meses necessários para que o valor
# pertencente a João iguale ou ultrapasse o valor pertencente a Carlos.

SalarioCarlos = float(input("Digite o valor do salário de Carlos: "))
SalarioJoao = SalarioCarlos / 3
Meses = 0

while SalarioJoao <= SalarioCarlos:
  SalarioCarlos = SalarioCarlos * 1.02
  SalarioJoao = SalarioJoao * 1.05
  Meses = Meses + 1
  print("Meses: ", Meses, "Valor Carlos: ",SalarioCarlos, "Valor João", SalarioJoao)