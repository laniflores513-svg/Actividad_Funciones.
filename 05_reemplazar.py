def reemplazar(texto, viejo, nuevo):
    return texto.replace(viejo, nuevo)


texto = input("Ingresa un texto: ")
viejo = input("Carácter a reemplazar: ")
nuevo = input("Nuevo carácter: ")

print("Resultado:", reemplazar(texto, viejo, nuevo))