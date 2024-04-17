#EJERCICIOS

#Programa para determinar el MCD de dos numeros enteros por el algoritmo de Euclides

print(
'''
Advertencia: para que el algoritmo funcione,
procure poner el numero mayor como el primer numero.
'''
)
numero1 = int(input("Ingresa el primer numero: "))
numero2 = int(input("Ingresa el segundo numero: "))

def mcd(dividendo, divisor):
    while divisor != 0:
        resto = dividendo % divisor #Primero se calcula el resto
        #Luego se divide el divisor entre el resto sucesivamente hasta que la division sea exacta
        dividendo = divisor 
        divisor = resto
    return dividendo

print(f"El MCD de {numero1} y {numero2} es: {mcd(numero1, numero2)}")
