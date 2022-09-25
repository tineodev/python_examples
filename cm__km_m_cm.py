
import math

print("CONVERTIDOR DE CM A KM, M Y CM")
cantidad = int(input("Escriba una cantidad en centímetros: "))


# * Comprueba que la cantidad ingresada no es cero, o negativo
if cantidad == 0:
  print("Escriba una distancia mayor que cero.")
  exit()
elif cantidad < 0:
  print("No existen distancias negativas.")
  exit()
else:
  pass


# * Funcion que saca la cantidad de km
if math.floor(cantidad/100000) != 0:
  cociente_km = math.floor(cantidad/100000)
  residuo_km = cantidad % 100000
else:
  cociente_km = 0
  residuo_km = cantidad


# * Funcion que saca la cantidad de m
if math.floor(residuo_km/100) != 0:
  cociente_m = math.floor(residuo_km/100)
  residuo_m = residuo_km % 100
else:
  cociente_m = 0
  residuo_m = residuo_km


# * Funcion que saca la cantidad de cm
residuo_cm = residuo_m


# * Imprime los resultados
print(f"{cantidad} centímetros son ", end="")


# * No imprime valores innecesarios
if cociente_km != 0:
  print(f"{cociente_km}km, ", end="")
if cociente_m != 0:
  print(f"{cociente_m}m, ", end="")
if residuo_cm !=0:
  print(f"{residuo_cm}cm.")

