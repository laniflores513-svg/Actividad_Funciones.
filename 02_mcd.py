def calcular_mcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a


num1 = int(input("Primer número: "))
num2 = int(input("Segundo número: "))

print("El MCD es:", calcular_mcd(num1, num2))
