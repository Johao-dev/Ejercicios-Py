#Algortimmo para calcular el factorial de un numero
#IMPORTANTE: El orden de los factores no altera el producto.
def factorial_calculator(entero):
    factorial = 1
    #Nos aseguramos de que no sea negativo o sea 1
    if entero < 0:
        return "no se puede calcular el factorial de un numero negativo"
    elif entero == 1:
        return 1
    else:
        for i in range(1, entero + 1):
            factorial *= i #Se mutiplica 1*2*3*4...*n (EL ORDEN DE LOS FACTORES NO ALTERA EL PRODUCTO.)
        return factorial
    
numero = int(input("Esriba un numero: "))
resultado = factorial_calculator(numero)
print(f"El factorial de {numero} es: {resultado}")