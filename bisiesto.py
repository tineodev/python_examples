
print("COMPROBADOR DE AÑOS BISIESTOS")

year = int(input("Escriba un año y le diré si es bisiesto: "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("El año es bisiesto porque es múltiplo de 4, 100 y de 400")
    else:
      print("El año no es bisiesto porque es múltiplo de 4, 100 y no de 400")
  else:
    print("El año es bisiesto porque es múltiplo de 4")
else:
  print("El año no es bisiesto porque no es múltiplo de 4")

