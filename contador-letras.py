#Algortimo para contar las ocurrencias de cada letra en una
#palabra ingresada por el teclad0.

#Diccionario que agregue o incremente las letras dadas en una palabra
ocurrencias = {}

def contador_ocurrencias(palabra):
    palabra = palabra.lower() #No distinguir entre mayusculas y minusculas
    #Si la letra esta en el diccionario aumentar en una unidad, si no, crear la letra con una unidad
    for letra in palabra:
        if letra in ocurrencias:
            ocurrencias[letra] += 1
        else:
            ocurrencias[letra] = 1
    #items(): Devuelve la clave y valor de un diccionario
    for letra, cantidad in ocurrencias.items():
        print(f"La letra '{letra}' aparece {cantidad} veces.")

palabra = input("Escriba una palabra: ")
contador_ocurrencias(palabra)
