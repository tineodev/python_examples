
# * Imported functions
from math import factorial



def run():
  # * Code
  number_user = int(input("Introduzca el número límite: "))

  if number_user <= 0:
    print("No se aceptan números negativos o el cero")
    exit()

  for i in range(1, number_user+1):
    if i == 1:
      print(f"{i} - La unidad")
    else:
      i_factorial = factorial(i-1)
      i_primo = (i_factorial+1) % i
      if i_primo == 0 :
        print(f"{i} - Primo")
      else:
        print(f"{i} - Compuesto")



if __name__ == "__main__":
  run()


