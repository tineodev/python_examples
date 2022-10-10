
# * Imported functions
from math import factorial



def run():
  # * Code
  # pass
  number_user = int(input("Introduzca el número a evaluar: "))

  if number_user <= 0:
    print("No se aceptan números negativos o el cero")
    exit()
  elif number_user == 1:
    print(f"{number_user} no es primo")
    exit()
  else:
    pass

  number_factorial = factorial(number_user-1)

  number_primo = (number_factorial+1) % number_user 

  if number_primo == 0 :
    print(f"{number_user} es primo")
  else:
    print(f"{number_user} no es primo")



if __name__ == "__main__":
  run()


