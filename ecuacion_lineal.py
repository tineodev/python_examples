
print("ECUACIÓN A X + B = 0")

pendiente = float(input("Escriba el valor de la pendiente: "))
intercepto = float(input("Escriba el valor del intercepto en el eje y: "))


if pendiente == 0 :
  print("La ecuación no tiene solución.")
  exit()
else:
  raiz = (-intercepto)/pendiente
  print(f"La ecuación tiene una solución: {raiz}")

