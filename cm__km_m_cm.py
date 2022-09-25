
import math

print("CONVERTIDOR DE CM A KM, M Y CM")

cantidad = int(input("Escriba una cantidad en centímetros: "))

if cantidad == 0:
  print("Escriba una distancia mayor que cero.")
  exit()
elif cantidad < 0:
  print("No existen distancias negativas.")
  exit()
else:
  pass


if math.floor(cantidad/100000) != 0:
  cociente_km = math.floor(cantidad/100000)
  residuo_km = cantidad % 100000
else:
  cociente_km = 0
  residuo_km = cantidad


if math.floor(residuo_km/100) != 0:
  cociente_m = math.floor(residuo_km/100)
  residuo_m = residuo_km % 100
else:
  cociente_m = 0
  residuo_m = residuo_km


residuo_cm = residuo_m

print(f"{cantidad} centímetros son {cociente_km}km {cociente_m}m {residuo_cm}cm")




