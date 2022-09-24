
print("CÁLCULO DE ÁREAS")

print("Elija una figura geométrica")
print("a) Triángulo")
print("b) Círculo")

eleccion_area = input("Qué figura quiere calcular (T o C)? ").lower().strip()

if eleccion_area == "t":
  base = float(input("Escriba la base: "))
  altura = float(input("Escriba la altura: "))
  area = base * altura * 0.5
  print(f"Un triángulo de base {base} y altura {altura} tiene un área de {area}")

elif eleccion_area =="c":
  radio = float(input("Escriba el radio: "))
  valor_pi = 3.141592
  area = valor_pi * (radio**2)
  print(f"Un círculo de radio {radio} tiene un área de {round(area, 2)}")

else:
  print("Escriba una opción correcta e inténtelo de nuevo.")

