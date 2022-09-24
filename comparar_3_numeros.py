
print("COMPARADOR DE TRE NÚMEROS")

numero_1 = float(input("Escriba un número: "))
numero_2 = float(input("Escriba otro número: "))
numero_3 = float(input("Escriba otro número más: "))



if numero_1 == numero_2 and numero_1 == numero_3:
  print("Ha escrito tres veces el mismo número.")

if numero_1 != numero_2 and numero_1 != numero_3 and numero_2 != numero_3:
  print("Los tres números que ha escrito son distintos")

if numero_1 == numero_2 and numero_2 != numero_3: 
  print("Ha escrito uno de los números dos veces")

if numero_1 != numero_2 and numero_2 == numero_3:
  print("Ha escrito uno de los números dos veces")

if numero_1 == numero_3 and numero_2 != numero_3:
  print("Ha escrito uno de los números dos veces")
