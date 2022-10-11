
# * Imported libraries
import random



# * Functions
def generar_password():
  MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
  MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
  NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
  CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

  CARACTERES = MAYUS + MINUS + NUMS + CHARS

  password = []
  
  for i in range(18):
    password_add = random.choice(CARACTERES)
    password.append(password_add)

  return "".join(password)

def run():
  # * Code
  # pass

  password_new = generar_password()
  print(f"Tu nueva contraseña es: {password_new}")


if __name__ == "__main__":
  run()


