#Programa para contar numeros pares e impares.
#Asignamos un punto de inicio
numero_impar= 0 
numero_par= 0 
numero= int(input("Introduce un numero o escribe 0 para detener: ")) #Introducir numero para iniciar el bucle.

while numero != 0: #Mientras el numero ingresado sea diferente de 0.
    if numero % 2 == 1: #Para saber si es impar dvididimos el numero entre 2, y si da uno es impar.
        numero_impar += 1 #Incrementamos el numero impar en 1
    else: #Si al dividir el numero entre 2 no da 1, entonces es par.
        numero_par += 1 #Incrementamos el numero par en 1
    numero= int(input("Introduce un numero o escribe 0 para detener: ")) #Para que el bucle siga.
#Si se introduce un 0 el bucle termina y se mostraran cuantos numeros
#pares e impares hay.
print("Cuenta de numeros impares: ", numero_impar)
print("Cuenta de numeros pares: ", numero_par)

