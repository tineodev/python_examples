
import random

print("OBTENER VALOR")

num_players = int(input("Número de jugadores: "))
if num_players < 1:
  print("¡Imposible!")
  exit()

num_valor = int(input("Valor a conseguir: "))
if num_valor > 6 or num_valor < 1:
  print(f"¡Imposible conseguir un {num_valor}!")
  exit()


for i in range(num_players):
  valor_dado = random.randint(1,6)

  if valor_dado == num_valor:
    print(f"Jugador {i+1}: {valor_dado} CONSEGUIDO")
  else:
    print(f"Jugador {i+1}: {valor_dado}")

