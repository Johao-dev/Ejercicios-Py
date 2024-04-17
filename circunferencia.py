#Algortimo para calcular la longitud de una circunferencia 
#con el radio dado
'''
variables:
    reales: pi, radio
'''
#Importamos pi
from math import pi

#Calculamos la longitud
def longitud_circulo(radio):
    return pi * radio**2

radio = float(input("Digite el radio de la circunferencia: "))
print(f"La longitud de la circunferencia es: {round(longitud_circulo(radio), 3)}")