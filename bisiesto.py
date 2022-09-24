
print("COMPROBADOR DE AÑOS BISIESTOS")

year = int(input("Escriba un año y le diré si es bisiesto: "))

if year % 4 == 0:
  if year % 400 == 0 and year % 100 != 0:
    print("El año es bisiesto")
  if year % 100 == 0:
    print("El año no es bisiesto")
  else:
    print("El año es bisiesto")
else:
  print("El año no es bisiesto")

# ! Resolver bug