print("COMPARADOR DE MÚLTIPLOS")

numero_1 = int(input("Escriba un número: "))
numero_2 = int(input("Escriba otro número: "))

if numero_1 < numero_2:
  mayor = numero_2
  menor = numero_1
elif numero_1 > numero_2:
  mayor = numero_1
  menor = numero_2
else:
  mayor = numero_1
  menor = numero_2

resultado = mayor % menor 

if resultado == 0:
  print(f"{mayor} es múltiplo de {menor}.")
else:
  print(f"{mayor} no es múltiplo de {menor}.")
