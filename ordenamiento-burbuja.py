lista = []
intercambio = True 
numeroElementos =  int(input("¿Cuantos elementos deseas ordenar?: "))

for i in range(numeroElementos):
    valorIngresado = float(input(f"Ingresa el elemento de la lista: "))
    lista.append(valorIngresado)

while intercambio:
    intercambio = False 
    for i in range(len(lista) - 1): 
        if lista[i] > lista[i + 1]: 
            intercambio = True 
            lista[i], lista[i + 1] = lista[i + 1], lista[i]

print("\nOrdenada:")
print(lista)
