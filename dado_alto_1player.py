
import random


print("EL DADO MÁS ALTO")


num_dados = int(input("Número de dados: "))
if num_dados < 1:
  print("¡Imposible!")
  exit()


dado_mayor = 1



print("Dados: ", end="")
for i in range(num_dados):
  dado_valor = random.randint (1, 6)
  print(f"{dado_valor} ", end="")

  if dado_mayor == dado_valor or dado_mayor < dado_valor:
    dado_mayor = dado_valor
print()


print(f"El dado más alto es {dado_mayor}")

