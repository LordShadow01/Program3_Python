print("Hola que tal, soy una calculadora básica bueno soy alguien que la hizo xd")

print("Esta mamada te va a ayudar a sumar, restar, multiplicar y dividir dos números ya mas es avaricia xd")
num1_str = input("Introduce el primer número: ")
num1 = float(num1_str) 


num2_str = input("Introduce el segundo número: ")
num2 = float(num2_str) 

# Realiza las operaciones
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2


if num2 != 0:
    division = num1 / num2
else:
    division = "No se puede dividir al menos que seas gojo jajaja"


print(f"\nResultados:")
print(f"Suma: {num1} + {num2} = {suma}")
print(f"Resta: {num1} - {num2} = {resta}")
print(f"Multiplicación: {num1} * {num2} = {multiplicacion}")
print(f"División: {num1} / {num2} = {division}")

print("Fin de esta mamada xd jajaja Ever se la come xd jajaja")