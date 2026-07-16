numeros = []

cantidad = int(input("¿Cuántos números vas a ingresar?: "))

if cantidad <= 0:
    print("Debes ingresar al menos un número.")
else:
    for i in range(cantidad):
        numero = float(input(f"Ingresa el número {i + 1}: "))
        numeros.append(numero)

    mayor = numeros[0]
    menor = numeros[0]

    for numero in numeros:
        if numero > mayor:
            mayor = numero

        if numero < menor:
            menor = numero

    print("\nLista ingresada:", numeros)
    print("El número mayor es:", mayor)
    print("El número menor es:", menor)