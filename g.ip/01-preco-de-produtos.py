# Tarefa 2. Estruturas condicionais e de repetição: Tabuada com entrada do usuário (FOR)
# Dev: Rafael Crispim
# Data: 5.9.2022

# Faça um programa que receba o preço, a categoria (1 – limpeza; 2 – alimentação; ou 3 – vestuário)
# e a situação (R – produtos que necessitam de refrigeração; e N – produtos que não necessitam de refrigeração). Calcule e mostre:
# O valor do aumento, usando as regras que se seguem.

# preço   categoria   percentual
#<= 25    1           5%
#         2           8%
#         3           10%
#> 25     1           12%
#         2           15%
#         3           18%

# O valor do imposto, usando as regras a seguir. O produto que preencher pelo menos um dos seguintes requisitos pagará imposto equivalente
# a 5% do preço; caso contrário, pagará 8%. Os requisitos são:
# Categoria: 2 Situação: R
# O novo preço, ou seja, o preço mais aumento menos imposto. A classificação, usando as regras a seguir.

# novo preço      classificação
# < = 50          Barato
# Entre 50 e 120  Normal
# > = 120         Caro

Preco = float(input("Digite o preço:"))
Categoria = int(input("Digite a categoria (1 - limpeza, 2 - alimentação, 3 -  vestuário):"))
Situacao = input("Digite a situação (R - refrigerado, N - não refrigerado):")
if Preco < 25:
  if Categoria == 1:
    PrecoComAumento = Preco * 1.05
    NovoPreco = PrecoComAumento * (1 - 0.05)
    if NovoPreco <= 50:
      print("Barato")
    elif NovoPreco > 50 and NovoPreco <= 120:
      print("Normal")
    else:
      print("Caro")
  elif Categoria == 2 or Situacao == "R":
    PrecoComAumento = Preco * 1.08
    NovoPreco = PrecoComAumento * (1 - 0.05)
    if NovoPreco <= 50:
      print("Barato")
    elif NovoPreco > 50 and NovoPreco <= 120:
      print("Normal")
    else:
      print("Caro")
  else:
    PrecoComAumento = Preco * 1.10
    NovoPreco = PrecoComAumento * (1 - 0.05)
    if NovoPreco <= 50:
      print("Barato")
    elif NovoPreco > 50 and NovoPreco <= 120:
      print("Normal")
    else:
      print("Caro")
else:
  if Categoria == 1:
    PrecoComAumento = Preco * 1.12
    NovoPreco = PrecoComAumento * (1 - 0.05)
    if NovoPreco <= 50:
      print("Barato")
    elif NovoPreco > 50 and NovoPreco <= 120:
      print("Normal")
    else:
      print("Caro")
  elif Categoria == 2 or Situacao == "R":
    PrecoComAumento = Preco * 1.15
    NovoPreco = PrecoComAumento * (1 - 0.05)
    if NovoPreco <= 50:
      print("Barato")
    elif NovoPreco > 50 and NovoPreco <= 120:
      print("Normal")
    else:
      print("Caro")
  else:
    PrecoComAumento = Preco * 1.18
    NovoPreco = PrecoComAumento * (1 - 0.05)
    if NovoPreco <= 50:
      print("Barato")
    elif NovoPreco > 50 and NovoPreco <= 120:
      print("Normal")
    else:
      print("Caro")