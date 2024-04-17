#Algortimo que muestre 100 numeros naturales aleatorios y determine
#cuantos son menores que 15, cuantos son mayores que 50 y cuantos estan comprendidos entre 25 y 45

import random

#Creamos lista y variables a usar
cien_numeros = [random.randint(1, 100) for _ in range(100)]
menores_15 = 0
mayores_50 = 0
comprendidos_25_45 = 0

print(f"Lista: {cien_numeros}")

#Aplicamos los filtros pedidos
for numero in cien_numeros:
    if numero < 15:
        menores_15 += 1
    elif numero > 50:
        mayores_50 += 1
    elif 25 < numero < 45:
        comprendidos_25_45 += 1

#Mostramos resultados
print(f"Hay {menores_15} numeros menores que 15 en la lista")
print(f"Hay {mayores_50} numeros mayores que 50 en la lista")
print(f"Hay {comprendidos_25_45} numeros comprendidos entre 25 y 45 en la lista.")