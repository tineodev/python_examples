
import random


print("EL DADO MÁS ALTO - 2 PLAYER")

# * Input numero de dados
num_dados = int(input("Número de dados: "))
if num_dados < 1:
  print("¡Imposible!")
  exit()


# * Lista de valor mayor de cada uno & dado mayor inicial
dados_mayores = []
dado_mayor = 1


# * Bucle para 2 jugadores (ampliable a más)
for i in range(2):
  print(f"Jugador {i+1}: ", end="")

  # * Bucle para valores de dados de cada jugador
  for j in range(num_dados):
    dado_valor = random.randint(1,6)
    print(f"{dado_valor} ", end="")

    if dado_mayor == dado_valor or dado_mayor < dado_valor:
      dado_mayor = dado_valor


  # * Añade a la lista con los mayores valores de cada jugador
  dados_mayores += [dado_mayor]

  print()


# * Evalua los valores mayores de cada uno (ampliable a mas)
if dados_mayores[0] > dados_mayores[1]:
  print("Ha ganado el jugador 1")
elif dados_mayores[0] < dados_mayores[1]:
  print("Ha ganado el jugador 2")
else:
  print("Han empatado")

