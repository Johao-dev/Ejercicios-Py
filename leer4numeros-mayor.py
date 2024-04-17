#Algoritmo que pide al usuario que ingrese 4 numeros y muestre
#el mayor de los 4 

numeros = []
numero1 = int(input("Ingrese primer numero: "))
numeros.append(numero1)
numero2 = int(input("Ingrese segundo numero: "))
numeros.append(numero2)
numero3 = int(input("Ingrese tercer numero: "))
numeros.append(numero3)
numero4 = int(input("Ingrese cuarto numero: "))
numeros.append(numero4)

print(f"Los numeros ingresados son: {numeros}")
print(f"El mayor de los 4 numeros es: {max(numeros)}")