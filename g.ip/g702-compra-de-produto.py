# Tarefa 2. Estruturas condicionais e de repetição: Compra de produto (Switch Case)
# Dev: Rafael Crispim
# Data: 5.9.2022

# Faça um programa que receba:
# O código do produto comprado; e
# A quantidade comprada do produto.
# Calcule e mostre:

# O preço unitário do produto comprado, seguindo a Tabela abaixo;
# O preço total da nota;
# O valor do desconto, seguindo a Tabela abaixo e aplicado sobre o preço total da nota; e
# O preço final da nota depois do desconto.

# CÓDIGO      PREÇO     PREÇO TOTAL DA NOTA         % DE DESCONTO
# 1 a 10      R$10,00   Até R$250,00                5%
# 11 a 20     R$15,00   Entre R$250,00 e R$500,00   10%
# 21 a 30     R$20,00   Acima de R$500,00           15%
# 31 a 40     R$30,00

Codigo = int(input("Digite o código: "))
Quantidade = int(input("Digite a quantidade: "))

if Codigo >= 1 and Codigo <= 10:
    Preco = 10
    PrecoNota = Preco * Quantidade
    if PrecoNota <= 250:
        Desconto = PrecoNota * 0.05
        PrecoFinal = PrecoNota * (1 - 0.05)
    else:
        Desconto = PrecoNota * 0
        PrecoFinal = PrecoNota

elif Codigo >= 11 and Codigo <= 20:
    Preco = 15
    PrecoNota = Preco * Quantidade
    if PrecoNota > 250 and PrecoNota <= 500:
        Desconto = PrecoNota * 0.10
        PrecoFinal = PrecoNota * (1 - 0.10)
    else:
        Desconto = PrecoNota * 0
        PrecoFinal = PrecoNota

elif Codigo >= 21 and Codigo <= 30:
    Preco = 20
    PrecoNota = Preco * Quantidade
    if PrecoNota > 500:
        Desconto = PrecoNota * 0.15
        PrecoFinal = PrecoNota * (1 - 0.15)
    else:
        Desconto = PrecoNota * 0
        PrecoFinal = PrecoNota

elif Codigo >= 31 and Codigo <= 40:
    Preco = 30
    PrecoNota = Preco * Quantidade
    Desconto = PrecoNota * 0
    PrecoFinal = PrecoNota

print("Preço un.: R$", Preco, "Preço total: R$", PrecoNota, "Desconto: R$", Desconto, "Preço com desconto: R$",
      PrecoFinal)