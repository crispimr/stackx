# Tarefa 3. Idade de um nadador (IF)
# Dev: Rafael Crispim
# Data: 4.9.2022

# Faça um programa que receba a idade de um nadador e mostre sua categoria,
# usando as regras a seguir. Para idade inferior a 5, qual mensagem deveríamos mostrar?
# CATEGORIA     IDADE
# Infantil      5 a 7
# Juvenil       8 a 10
# Adolescente   11 a 15
# Adulto        16 a 30
# Sênior        Acima de 30

idade = int(input("Digite sua idade: "))
if idade < 5:
  print("Para a idade de", idade,"não há categoria")
elif idade >= 5 and idade <= 7:
  categoria = "Infantil"
elif idade >= 8 and idade <= 10:
  categoria = "Juvenil"
elif idade >= 11 and idade <= 15:
  categoria = "Adolescente"
elif idade >= 16 and idade <= 30:
  categoria = "Adulto"
else:
  categoria = "Sênior"

print("Para a idade de", idade,"a categoria é", categoria)
