#Algoritmo que lee 3 numeros y descubre si uno de ellos es
#la suma de los otros 2

def descubridor3000(numero1, numero2, numero3):
    if (numero1 + numero2 == numero3):
        print(f"{numero3} es la suma de {numero1} con {numero2}")
    elif (numero2 + numero3 == numero1):
        print(f"{numero1} es la suma de {numero2} con {numero3}")
    elif (numero3 + numero1 == numero2):
        print(f"{numero2} es la suma de {numero3} con {numero1}")
    else:
        print("Ningun numero es la suma de los otros dos.")

numero_1 = int(input("Ingrese primer numero: "))
numero_2 = int(input("Ingrese segundo numero: "))
numero_3 = int(input("Ingrese tercer numero: "))

descubridor3000(numero_1, numero_2, numero_3)



