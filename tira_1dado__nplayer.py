
import random


print("TIRADAS DE DADO")


num_jugadores = int(input("Número de jugadores: "))
if num_jugadores == 1:
  print("¡Imposible!")
  exit()


for i in range(num_jugadores):
  valor_dado = random.randint(1,6)
  print(f"Jugador {i+1}: {valor_dado}")

