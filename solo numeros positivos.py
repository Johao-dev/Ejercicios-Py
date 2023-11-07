#Programa para escribir numeros positivos y contar cuantos numeros ingresaste.
contador= 0 
numero= int(input("Ingrese cualquier numero, menos uno negativo: "))

while numero > 0: #Mientras el numero sea mayor a 0 (osea positivo)
    contador += 1 #El contador aumentara 
    numero= int(input("Ingrese cualquier numero, menos uno negativo: ")) #Y continuaras en el bucle
    if numero <= -1: #Si el numero es mayor a -1.
        print("Te dije solo numeros positivos bro...")
        break #Se detiene el programa
#Para saber cuantos numeros ingresaste.
if contador != 0: #Si el contador es difernte de cero (osea ingresaste mas de un numero xd)
    print("Ingresaste:", contador, "numeros")
else: #Si el contador es igual a o, pues...
    print("no ingresaste ningun numero.")
