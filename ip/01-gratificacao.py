#
# Dev: Rafael Crispim
# Data: 4.9.2022
# Uma empresa decidiu dar uma gratificação de Natal a seus funcionários, baseada no
# número de horas extras e no número de horas que o funcionário faltou ao trabalho.
# O valor do prêmio é obtido pela consulta à tabela que se segue, na qual:
# H = número de horas extras – (2/3 * ( número de horas falta ))
# H (MINUTOS	    PRÊMIO (R$)
# >= 2.401	        500,00
# 1.801 até 2.400   400,00
# 1.201 até 1.800   300,00
# 600 até 1.200     200,00
# <600	            100,00

horasExtras = float(input("Digite o número de horas extras: "))
horasFaltas = float(input("Digite o número de horas faltas: "))
totalHoras = (horasExtras - (2 / 3 * (horasFaltas))) * 60
if totalHoras >= 2401:
    premio = 500
elif totalHoras >= 1801 and totalHoras <= 2400:
    premio = 400
elif totalHoras >= 1201 and totalHoras <= 1800:
    premio = 300
elif totalHoras >= 600 and totalHoras <= 1200:
    premio = 200
else:
    premio = 100
print("Total minutos:", totalHoras, "Prêmio: R$", premio)
