import time
import random

print("JUEGO DE DADOS - 2 JUGADORES")


# * 2 jugadores
player_1 = input("Jugador 01, introduzca su nombre: ")
player_2 = input("Jugador 02, introduzca su nombre: ")


time.sleep(1)
print("¡Qué comience el juego!")


# * Dados player_1
p1_dado1 = random.randint(1,6)
p1_dado2 = random.randint(1,6)
puntaje_p1 = p1_dado1 + p1_dado2
time.sleep(1)
print(f"{player_1} ha sacado un {p1_dado1} y un {p1_dado2}")


# * Dados player_2
p2_dado1 = random.randint(1,6)
p2_dado2 = random.randint(1,6)
puntaje_p2 = p2_dado1 + p2_dado2
time.sleep(1)
print(f"{player_2} ha sacado un {p2_dado1} y un {p2_dado2}")


# * Comparacion dados player_1


# * Comparacion dados player_2


# * Comparacion dados
time.sleep(1)
if puntaje_p1 > puntaje_p2:
  print(f"Ha ganado {player_1}")
elif puntaje_p1 < puntaje_p2:
  print(f"Ha ganado {player_2}")
else:
  pass
