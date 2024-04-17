#Algoritmo para calcular la superficie de un triangulo en
#funcion de la base y la altura S = (base*altura)/2
'''
variables:
    reales = base, altura, superficie
'''
#Funcion que calcule la superficie
def superficie(base, altura):
    return (base * altura) / 2

base = float(input("Digite la base del triangulo: "))
altura = float(input("Digite la altura del triangulo: "))
print(f"La superficie del triangulo es: {superficie(base, altura)}")