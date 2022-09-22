
import math

print("DIVISOR DE NÚMEROS")

dividendo = int(input("Escriba el dividendo: "))
divisor = int(input("Escriba el divisor: "))

if divisor == 0:
  print("No se puede dividir por cero.")
  exit()

cociente = dividendo / divisor
resto = dividendo % divisor


if resto != 0 :
  cociente = math.floor(cociente)
  print(f"La división no es exacta. Cociente: {cociente} Resto: {resto}")
else:
  print(f"La división es exacta. Cociente {int(cociente)}")

