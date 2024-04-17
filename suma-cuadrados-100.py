#Algoritmo que suma los cuadrados de los 100 primeros numeros primos

cuadrados = [x**2 for x in range(1, 101)] #En un rango de 1 al 100 para cada valor de x, regresarla al cuadrado.
sumas = sum(cuadrados)
print(f"La suma de los cuadrados de los 100 primeros numeros naturales es: {sumas}")
