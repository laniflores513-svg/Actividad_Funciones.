import math

def raiz(numero):
    if numero < 0:
        return "No existe raíz cuadrada real."
    return math.sqrt(numero)


numero = float(input("Ingresa un número: "))

print("Resultado:", raiz(numero))