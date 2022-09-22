
import math
print("CONVERTIDOR DE SEGUNDOS A HORAS Y MINUTOS")

entrante = int(input("Escriba una cantidad de segundos: "))

horas = math.floor(entrante/3600)

minutos = math.floor((entrante%3600)/60)

segundos = math.floor((entrante%3600)%60)

print(f"{entrante} segundos son {horas} horas, {minutos} minutos y {segundos} segundos")


