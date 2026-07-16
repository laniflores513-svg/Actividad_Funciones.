numeros = []

cantidad = int(input("¿Cuántos números vas a ingresar?: "))

for i in range(cantidad):
    numero = int(input(f"Ingresa el número {i + 1}: "))
    numeros.append(numero)

pares = 0
impares = 0

for numero in numeros:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("\nLista ingresada:", numeros)
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)