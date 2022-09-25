
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


# * Valores obtenidos & puntaje player2
p2_valor1 = random.choice(lista_game15)
p2_valor2 = random.choice(lista_game15)
p2_valor3 = random.choice(lista_game15)
p2_puntaje = p2_valor1 + p2_valor2 + p2_valor3

