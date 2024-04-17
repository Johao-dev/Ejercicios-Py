#Algoritmo para saber si un palabra es palindromo o no

#Definimos una funcion que lo que hara es invertir la palabra que ingresemos
def invertir_cadena(cadena):
    return cadena[::-1] # [::-1]: Es una tecnica se slicing que se utiliza para revertir una secuencia (string, lista, tupla)
                        #Estructura de un slicing: [start:stop:step].

#Definimos una funcion que verificara si la palabra es polindromo o no
def palindromo(palabra):
    palabra = palabra.replace(" ", "") #replace(): reemplaza el primer argumento con el segundo en este caso reemplaza los espacios con 'sin espacios'
    if palabra == invertir_cadena(palabra): #Si la palabra es igual a su inverso
        print("La palabra es polindroma.")
    else:
        print("La palabra no es polindroma.")

print("Algortimo para averiguar si una palara es palindromo o no :D")
print("Para terminar ingrese terminar.")

while True:
    averiguar = input("Ingrese una palabra: ").lower()
    if averiguar == "terminar":
        break
    palindromo(averiguar)
    
