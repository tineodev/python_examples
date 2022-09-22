
print("CÁLCULO DEL ŃDICE DE MASA CORPORAL (IMC)")

peso = int(input("¿Cuánto pesa? "))
estatura = float(input("¿Cuánto mide(metros)? "))

imc = round(peso / estatura**2 , 1)

print(f"Su imc es {imc}")
print("Un imc muy alto indica obesidad. Los valores normales de imc están entre 20 y 25, pero esos límites dependen de la edad, del sexo, de la constitución física, etc.")

