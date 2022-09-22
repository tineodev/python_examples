
import math

print("DIVISOR DE NÚMEROS")

dividendo = int(input("Escriba el dividendo: "))
divisor = int(input("Escriba el divisor: "))


cociente = dividendo / divisor
resto = dividendo % divisor


if resto != 0 :
  cociente = math.floor(cociente)
  print(f"La división no es exacta. Cociente: {cociente} Resto: {resto}")
else:
  print(f"La división es exacta. Cociente {int(cociente)}")

