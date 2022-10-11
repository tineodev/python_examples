
# * Imported libraries
import random



# * Functions




def run():
  # * Code
  # pass
  number_key = random.randint(1,100)


  print("Adivina el número (1 al 100)")
  number_user = int(input("Introduzca el número correcto: "))


  while number_key != number_user:

    if number_user <= 0 or number_user > 100:
      number_user = int(input("Introduzca un número entre el 1 y el 100: "))


    elif number_key > number_user:
      number_user = int(input("Introduzca un número más grande: "))

    elif number_key < number_user:
      number_user = int(input("Introduzca un número más pequeño: "))


  print("Ganaste")

if __name__ == "__main__":
  run()


