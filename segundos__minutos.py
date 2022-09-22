import math

print("CONVERTIDOR DE SEGUNDOS A MINUTOS")

entrante = int(input("Escriba una cantidad de segundos: "))

minutos = int(math.floor(entrante/60))

segundos = int(entrante%60)

print(f"{entrante} segundos son {minutos} minutos y {segundos} segundos")