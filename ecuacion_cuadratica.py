
print("ECUACIÓN A X^2 + B X + C = 0")

coef_principal = int(input("Introduzca el coeficiente principal: "))
coef_lineal = int(input("Introduzca el coeficiente lineal: "))
coef_independiente = int(input("Introduzca el término independiente: "))


if coef_principal == 0:
  print("El coeficiente principal no puede ser cero")
  exit()


discriminante = coef_lineal**2 - 4*(coef_principal * coef_independiente)


if discriminante < 0:
  print("La ecuación no tiene raíces reales")
elif discriminante ==0:
  raiz_mayor = (-coef_lineal + (discriminante**0.5))/(2*coef_principal)

  print("La ecuación tiene 1 raíz real")
  print(f"La raíz es {raiz_mayor}")
else:
  print(discriminante)
  raiz_mayor = (-coef_lineal + discriminante**0.5)/(2*coef_principal)
  raiz_menor = (-coef_lineal - discriminante**0.5)/(2*coef_principal)
  print("La ecuación tiene 2 raíces reales")
  print(f"Las raíces son {raiz_mayor} y {raiz_menor}")

