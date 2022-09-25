import time
import random

print("JUEGO DE DADOS - 2 JUGADORES")


player_1 = input("Jugador 01, introduzca su nombre: ")
player_2 = input("Jugador 02, introduzca su nombre: ")


time.sleep(1)
print("¡Qué comience el juego!")


dado_p1 = random.randint(1,6)
time.sleep(1)
print(f"{player_1} ha sacado un {dado_p1}")
dado_p2 = random.randint(1,6)
time.sleep(1)
print(f"{player_2} ha sacado un {dado_p2}")


time.sleep(1)
if dado_p1 < dado_p2:
  print(f"Ha ganado {player_2}")
elif dado_p1 > dado_p2:
  print(f"Ha ganado {player_1}")
else:
  print("Han empatado")

