# Tarefa 9. Idade para voto (IF)
# Dev: Rafael Crispim
# Data: 5.9.2022

# Escreva um programa para ler o ano de nascimento de uma pessoa
# e escrever uma mensagem que diga se ela poderá ou não votar este ano
# (não é necessário considerar o mês em que ela nasceu).

ano = int(input("Digite o ano de seu nascimento:"))
if ano <= 2006:
  print("Pode votar :(")
else:
  print("Não pode votar :)")