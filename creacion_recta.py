
print("LISTAS DESDE CERO HASTA VALOR")

valor = int(input("Escriba un número entero: "))


if valor > 0:
  lista = range(0, valor+1)
  print(list(lista))
elif valor < 0:
  lista = range(0, valor-1, -1)
  print(list(lista))
else:
  lista = range(0, valor+1)
  print(list(lista))

