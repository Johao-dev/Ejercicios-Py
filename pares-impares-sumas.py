#Algortimo que suma independientemente los numeros pares e impares
#del 1 al 200 
'''
variables:
    reales: sumas_pares, sumas_impares
    listas: pares, impares
'''
#contadoras para ir sumando por separado
sumas_pares = 0
sumas_impares = 0

for numeros_pares_impares in range(1, 201):
    #depende de si el nuemro es par se agrega a la lista de pares y si no lo es se agrega a la otra lista
    if numeros_pares_impares % 2 == 0:
        sumas_pares += numeros_pares_impares
    else: 
        sumas_impares += numeros_pares_impares
        
#Mostramos el resultado
print(f"La suma de los numeros pares del 1 al 200 es: {sumas_pares}")
print(f"La suma de los numeros impares del 1 al 200 es: {sumas_impares}")