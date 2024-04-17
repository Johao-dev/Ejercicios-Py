#Algortimo que muestra la suma y producto de los numeros comprendidos 
#entre 20 y 400, incluyendolos.

sumas = 0
producto = 1

for i in range(20, 401, 2):
    sumas += i
    producto *= i

print(f"La suma de los numeros pares comprendidos entre 20 y 400, incluyendolos a ambos es {sumas} y el producto es {producto}")