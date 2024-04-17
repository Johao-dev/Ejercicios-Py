#Algortimo para resolver ecuaciones de segundo grado
'''
var
    reales = a, b, c
'''

from math import sqrt

a = float(input("Escribe el valor del termino principsl: "))
b = float(input("Escribe el valor del termino lineal: "))
c = float(input("Escribe el valor del termino independiente: "))

d = b**2 - 4*a*c #Calcular el valor dentro de la raiz

if d < 0:
    print("raices complejas.") #raiz cuadrada de un numero negativo
else:
    if d == 0:
        print(f"El resultado es: {-b / (2*a)}")
    else:
        print(f"El primer valor es: {(-b - sqrt(d)) / (2 * a)}")
        print(f"El segundo valor es: {(-b + sqrt(d)) / (2 * a)}")
