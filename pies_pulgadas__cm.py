
from unittest import result


print("CONVERTIDO DE PIES Y PULGADAS A CENTÍMETROS")

pies = int(input("Escriba una cantidad de pies: "))
pulgadas = int(input("Escriba una cantidad de pulgadas: "))

pies_cm = pies * 12 * 2.54
pulgadas_cm = pulgadas * 2.54

resultado = pies_cm + pulgadas_cm

print(f"{pies} pies y {pulgadas} pulgadas son {resultado}cm")
