
print("COMPARADOR DE NÚMEROS")

numero1 = float(input("Escriba un número: "))
numero2 = float(input("Escriba otro número: "))

if numero1 > numero2 :
  print(f"Menor: {numero2}; Mayor: {numero1}")
elif numero1 < numero2 :
  print(f"Menor: {numero1}; Mayor: {numero2}")
else: 
  print("Los dos números son iguales.")