#Programa para calcular si es un año bisiesto o año comun.
year = int(input("Introduce un año: "))

if year % 4 != 0: #Si el modulo(residuo) del año dividido entre 4 es diferente de 0.
    print("Año comun")
elif year < 1582: #A partir de 1582 se implemento este calculo para conocer los años.
    print("No dentro del periodo del calendario gregoriano.")
elif year % 100 != 0: #Si el modulo del año dividido entre 100 es diferente de 0.
    print("Año bisiesto")
elif year % 400 != 0: #Si el modulo del año dividido entre 400 es diferente de 0.
    print("Año comun")
else: #Si no cumple con ninguna de las condiciones anteriores.
    print("Año bisiesto")


