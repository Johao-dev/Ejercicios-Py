a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))
c = int(input("Ingrese un ultimo numero: "))

if (b < a < c) or (c < a < b):
    print(f"El numero central es {a}")
elif (a < b < c) or (c < b < a):
    print(f"El numero central es {b}")
else:
    print(f"El numero central es {c}")