numeros = []

cantidad = int(input("¿Cuántos números vas a ingresar?: "))

for i in range(cantidad):
    numero = float(input(f"Ingresa el número {i + 1}: "))
    numeros.append(numero)

suma = 0

for numero in numeros:
    suma += numero

print("\nLista ingresada:", numeros)
print("La suma de los elementos es:", suma)