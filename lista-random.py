#Algortimo que muestra 10 numeros enteros y separa los numeros pares
#y los impares, ademas muestra la media artimetica de los numeros impares
import random

#Listas a usar
lista_enteros = []
lista_pares = []
lista_impares = []

#Generamos los numeros enteros
for i in range(10):
    entero = random.randint(1, 100)
    lista_enteros.append(entero)

#Agregamos a las listas dependiendo si es par o no el numero iterado
for i in lista_enteros:
    if i % 2 == 0:
        lista_pares.append(i)
    else:
        lista_impares.append(i)

#Mostrando resultados
print(f"La lista es: {lista_enteros}")
print(f"hay {len(lista_pares)} numeros pares en la lista, y son los siguientes: {lista_pares}")
print(f"La media aritmetica de los numeros impares de la lista es: {sum(lista_impares) / len(lista_impares)}")