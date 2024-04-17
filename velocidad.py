#Algoritmo para calcular la velocidad de corredores

def calcular_velocidad(minutos, segundos):
    final = minutos*60 + segundos
    metros_carrera = 1500
    velocidad_media = metros_carrera/ final

    print(f"Tiempo hecho: {minutos} min {segundos} seg")
    print(f"Velocidad media: {velocidad_media:.2f} m/s.")

while True:
    minutos, segundos = map(int, input("Ingrese el tiempo (minutos y segundos) o 00 para finalizar: ").split())
    if minutos == 0 and segundos == 0:
        break

    calcular_velocidad(minutos, segundos)

#map(): Aplica una funcion a todos los elementos de uno o mas iterables y devuelve un 
#objeto map.