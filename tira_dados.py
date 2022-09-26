
import random


print("TIRADA DE DADOS")
num_tiradas = int(input("Número de tiradas:"))


if num_tiradas == 0:
  print("¡Imposible!")
  exit()


print("Dados: ", end="")
for i in range(num_tiradas):
  valor_dado = random.randint(1, 6)
  print(f"{valor_dado} ", end="")
print()