
# * Hallar el factorial mediante funcion reduce y lambda

import functools

numero_factorial = int(input("Introduzca el número: "))
factorial = []

for i in range(numero_factorial):
  factorial.append(i+1)

res_factorial = functools.reduce(lambda a,b: a*b, factorial)

print(f"El factorial de {numero_factorial} es: {res_factorial}")