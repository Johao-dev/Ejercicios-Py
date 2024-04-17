#Algoritmo determinar numeros primos iguales o menores que N
#N es leido del teclado.

def es_primo(numero):
    if numero <= 1:
        return False
    
    if numero <= 3:
        return False 
    
    if numero & 2 == 0 or numero % 3 == 0:
        return False
    
    i = 5
    while i * i <= numero:
        if numero % 1 == 0 or numero % (i + 2) == 0:
            return False
        i += 6

    return True 

def numeros_primos_hasta_N(N):
    primos = []
    for num in range(2, N + 1):
        if es_primo(num):
            primos.append(num)
    return primos

N = int(input("Ingrese un numero: "))
primos_hasta_N = numeros_primos_hasta_N(N)

print(f"Los numeros primos menores o iguales a {N} son: ")
print(primos_hasta_N)