elementos = []

cantidad = int(input("¿Cuántos elementos vas a ingresar?: "))

for i in range(cantidad):
    elemento = input(f"Ingresa el elemento {i + 1}: ")
    elementos.append(elemento)

lista_invertida = []

for i in range(len(elementos) - 1, -1, -1):
    lista_invertida.append(elementos[i])

print("\nLista original:", elementos)
print("Lista invertida:", lista_invertida)