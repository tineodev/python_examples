
print("PAR E IMPAR (1)")


numero1 = int(input("Escriba un número par: "))

if numero1 % 2 != 0:
  print("No ha escrito un número par.")
  print("Ejecute de nuevo el programa para volver a intentarlo.")
  exit()


numero2 = int(input("Escriba un número impar: "))

if numero2 % 2 == 0:
  print("No ha escrito un número impar.")
  print("Ejecute de nuevo el programa para volver a intentarlo.")
  exit()


print("¡Gracias por su colaboración!")

