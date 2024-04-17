#Algoritmo que lee 500 numeros enteros y visualiza los numeros negativos

numeros_positivos = 0

for i in range(500):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    
    if numero > 0:
        numeros_positivos += 1
print(f"La cantidad de números positivos ingresados es: {numeros_positivos}")