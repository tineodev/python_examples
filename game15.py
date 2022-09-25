
import random
lista_game15 = range(1,11)

print("JUEGO DEL QUINCE")


# * 2 jugadores
player_1 = input("Jugador 01, introduzca su nombre: ")
player_2 = input("Jugador 02, introduzca su nombre: ")


# * Valores obtenidos & puntaje player1
p1_valor1 = random.choice(lista_game15)
p1_valor2 = random.choice(lista_game15)
p1_valor3 = random.choice(lista_game15)
p1_puntaje = p1_valor1 + p1_valor2 + p1_valor3
print(f"{player_1} ha sacado {p1_valor1}, {p1_valor2} y {p1_valor3}")


# * Valores obtenidos & puntaje player2
p2_valor1 = random.choice(lista_game15)
p2_valor2 = random.choice(lista_game15)
p2_valor3 = random.choice(lista_game15)
p2_puntaje = p2_valor1 + p2_valor2 + p2_valor3
print(f"{player_2} ha sacado {p2_valor1}, {p2_valor2} y {p2_valor3}")


# * Comparacion puntajes > 15, y demas
if p1_puntaje > 15 and p2_puntaje > 15:
  print("No ha ganado nadie.")
elif p1_puntaje > 15:
  print(f"Ha ganado {player_2}")
elif p2_puntaje > 15:
  print(f"Ha ganado {player_1}")
else:
  if p1_puntaje > p2_puntaje:
    print(f"Ha ganado {player_1}")
  elif p1_puntaje < p2_puntaje:
    print(f"Ha ganado {player_2}")
  else:
    print("Han empatado")
