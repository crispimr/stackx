# Tarefa 5: Empresa com 10 funcionários (While)
# Dev: Rafael Crispim
# Data: 5.9.2022

# Uma empresa possui dez funcionários com as seguintes características:
# código, número de horas trabalhadas no mês,
# turno de trabalho (M – matutino; V – vespertino; N – noturno),
# categoria (O – operário; ou G – gerente), valor da hora trabalhada.
# Sabendo-se que essa empresa deseja informatizar sua folha de pagamento,
# faça um programa que:
# a) Leia as informações dos funcionários, exceto o valor da hora trabalhada,
# não permitindo que sejam informações dos turnos e nem categorias inexistentes.
# Trabalhe sempre com a digitação de letras maiúsculas;
# b) Calcule o valor da hora trabalhada, conforme a tabela 1.
# Adote o valor de R$450,00 para o salário mínimo;
# c) Calcule o salário inicial dos funcionários com base no valor da hora trabalhada
# e no número de horas trabalhadas;
# d) Calcule o valor do auxílio alimentação recebido pelo funcionário
# de acordo com seu salário inicial, conforme a tabela 2;
# e) Mostre o código, número de horas trabalhadas, valor da hora trabalhada,
# salário inicial, auxílio alimentação e salário final (salário inicial + auxílio alimentação).
# Tabela 1
# CATEGORIA TURNO   VALOR DA HORA TRABALHADA
# G         N       18% do salário mínimo
# G         M ou V  15% do salário mínimo
# O         N       13% do salário mínimo
# O         M ou V  10% do salário mínimo
# Tabela 2
# SALÁRIO INICIAL           AUXÍLIO ALIMENTAÇÃO
# Até R$300,00              20% do salário inicial
# Entre R$300,00 e R$600,00 15% do salário inicial
# Acima de R$600,00         5% do salário inicial

Laco1 = 1
Laco2 = True
Laco3 = True

SalarioMinimo = 450

while Laco1 <= 10:
    Codigo = int(input("Digite o código do funcionário: "))
    HorasTrabalhadas = float(input("Digite o número de horas trabalhadas: "))

    while Laco2:
        Turno = input("Digite o turno de trabalho (M, V, ou N): ")
        if Turno == "M" or Turno == "V" or Turno == "N":
            Laco2 = False
        else:
            Turno = "Digite um turno de trabalho válido (M, V, ou N):"
    Laco2 = True

    while Laco3:
        Categoria = input("Digite a categoria do funcionário (O ou G): ")
        if Categoria == "O" or Categoria == "G":
            Laco3 = False
        else:
            Categoria = "Digite uma categoria válida (O ou G)"
    Laco3 = True

    if Categoria == "G":
        if Turno == "N":
            ValorHora = SalarioMinimo * 0.18
        else:
            ValorHora = SalarioMinimo * 0.15
    else:
        if Turno == "N":
            ValorHora = SalarioMinimo * 0.13
        else:
            ValorHora = SalarioMinimo * 0.10

    SalarioInicial = ValorHora * HorasTrabalhadas
    if SalarioInicial <= 300:
        AuxilioAlimentacao = SalarioInicial * 0.20
    elif SalarioInicial > 300 and SalarioInicial <= 600:
        AuxilioAlimentacao = SalarioInicial * 0.15
    else:
        AuxilioAlimentacao = SalarioInicial * 0.05

    SalarioFinal = SalarioInicial + AuxilioAlimentacao

    print("\nCódigo: ", Codigo, "Horas trabalhadas: ", HorasTrabalhadas, "Valor hora", ValorHora)
    print("Salário inicial: ", SalarioInicial, "Auxílio alimentação", AuxilioAlimentacao, "Salário final:",
          SalarioFinal, "\n")

    Laco1 += Laco1