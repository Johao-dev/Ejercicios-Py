contador = 0

while True:
    numero = float(input("Ingresa un numero (0 para terminar): "))

    if numero == 0:
        break
    else:
        contador += 1

print(f"EL numero mayor es: {contador}")