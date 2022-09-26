
import random


print("OBTENER VALOR")


num_dados = int(input("Número de dados: "))
if num_dados < 1:
  print("¡Imposible!")
  exit()

num_valor = int(input("Valor a conseguir: "))
if num_valor < 1 or num_valor > 7:
  print(f"¡Imposible conseguir un {num_valor}!")
  exit()


desenlace = False


print("Dados: ", end="")
for i in range(num_dados):
  dado_valor = random.randint(1,6)
  print(f"{dado_valor} ", end="")
  if dado_valor == num_valor:
    desenlace = True
print()


if desenlace == True:
  print("El jugador ha ganado")
else:
  print("El jugador ha perdido")

