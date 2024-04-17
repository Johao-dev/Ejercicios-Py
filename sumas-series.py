#Algoritmo que visualice y sume la serie de 3,6,9,12,...,99
suma = 0

for numero in range(3, 100, 3): #Comienza el 3, termina en el 99 y tiene una separacion de 3 en 3
    print(numero) #para visualizar los numeros
    suma += numero #Suma el numero actual a la suma total

print(f'La suma de la serie "3,6,9,12,...,99" es igual a: {suma}')