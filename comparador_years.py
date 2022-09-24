
print("COMPARADOR DE AÑOS")

año_actual = int(input("¿En qué año estamos? "))
año_comparador = int(input("Escriba un año cualquiera: "))

diferencia = año_actual - año_comparador

if abs(diferencia) == 1:
  if año_actual < año_comparador:
    print(f"Para llegar al año {año_comparador} falta {abs(diferencia)} año.")
  else:
    print(f"Desde el año {año_comparador} ha pasado {diferencia} año.")

elif diferencia == 0:
  print("¡Son el mismo año!")

elif año_actual < año_comparador:
  print(f"Para llegar al año {año_comparador} falta {abs(diferencia)} años.")
else:
  print(f"Desde el año {año_comparador} han pasado {diferencia} años.")

