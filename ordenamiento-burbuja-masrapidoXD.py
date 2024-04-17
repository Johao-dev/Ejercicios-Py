#Ordenamiento burbuja

lista = []
num= int(input("¿Cuantos elementos deseas ordenar?: "))

for i in range(num):
    val = int(input("Agregar elemento: "))
    lista.append(val)

lista.sort()
print(lista)
