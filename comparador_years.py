
print("COMPARADOR DE AÑOS")

año_actual = int(input("¿En qué año estamos? "))
año_comparador = int(input("Escriba un año cualquiera: "))

if año_comparador < año_actual:
  diferencia = año_actual - año_comparador
  print(f"Desde el año {año_comparador} han pasado {diferencia} años.")

elif año_comparador == año_actual:
  print(f"¡Son el mismo año!")

else: 
  diferencia = año_comparador - año_actual
  print(f"Para llegar al año {año_comparador} faltan {diferencia} años.")