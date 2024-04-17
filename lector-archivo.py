def leer_archivo(name_archivo):
    try:
        with open(name_archivo, 'r') as archivo:
            for linea in archivo:
                yield linea.strip()
    except FileNotFoundError:
        print(f"El archivo '{name_archivo}' no se encontró.")

    

archivo = 'web.txt'
lineas = leer_archivo(archivo) 

for linea in lineas:
    print(linea)