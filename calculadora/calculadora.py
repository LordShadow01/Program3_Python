print("hola mundo") 
def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplica(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero no permitida"
def potencia(a, b):
    return a ** b 
def raiz_cuadrada(a):
    if a >= 0:
        return a ** 0.5
    else:
        return "Error: Raíz cuadrada de un número negativo no permitida"
def modulo(a, b):
    if b != 0:
        return a % b
    else:
        return "Error: Módulo por cero no permitido"
def calcular(operacion, a, b=None):
    if operacion == "suma":
        return suma(a, b)
    elif operacion == "resta":
        return resta(a, b)
    elif operacion == "multiplicacion":
        return multiplica(a, b)
    elif operacion == "division":
        return divide(a, b)
    elif operacion == "potencia":
        return potencia(a, b)
    elif operacion == "raiz_cuadrada":
        return raiz_cuadrada(a)
    elif operacion == "modulo":
        return modulo(a, b)
    else:
        return "Error: Operación no válida"