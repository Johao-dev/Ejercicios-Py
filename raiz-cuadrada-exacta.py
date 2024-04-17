#Algortimo que produce la raiz cuadrada de un numero introducido 
#por el teclado considerando si el numero puede ser negativo.
#SOLO FUNCIONA PARA RAICES CUADRADAS ENTERAS!

#Creamos un excepcion personalizada que hereda de la excepcion Exception
class NegativeNumberError(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

#Definimos la funcion que evaluara el numero y buscara su raiz
def raiz_cuadrada(n):
    if n < 0:
        raise NegativeNumberError("No existe solucion en los reales.")
    else:
        for i in range(1, n - 1):
            if i**2 == n:
                print(f"La raiz cuadrada de {n} es {i}")
            else: 
                continue

#Mostramos el resultado
try:
    numero = int(input("Ingrese un numero: "))
    raiz_cuadrada(numero)
except NegativeNumberError as e:
    print(f"Error: {e}")