# Tarefa 15. Complemento ao Polígono da tarefa 14 (IF)
# Dev: Rafael Crispim
# Data: 5.9.2022

# Acrescente as seguintes mensagens à solução da tarefa 14 conforme o caso.
# Caso o número de lados seja inferior a 3 escrever NÃO É UM POLÍGONO.
# Caso o número de lados seja superior a 5 escrever POLÍGONO NÃO IDENTIFICADO.

import math as m

n = int(input("Digite o número de lados:"))
md = float(input("Digite a medida em cm:"))
if n == 3:
  a = ((md * md) * m.sqrt(3))/4
  print("TRIÂNGULO com ", a, "cm2")
elif n == 4:
  a = md * md
  print("QUADRADO com ", a, "cm2")
elif n == 5:
  a = 5 * (md * md) / (4 * m.sqrt(5 - 2 * m.sqrt(5)))
  print("PENTÁGONO com ", a, "cm2")
elif n < 3:
  print("NÃO É UM POLÍGONO.")
else:
  print("POLÍGONO NÃO IDENTIFICADO.")