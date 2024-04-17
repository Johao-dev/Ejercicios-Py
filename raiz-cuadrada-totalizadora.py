def calcular_raiz_cuadrada(numero):
    if numero < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de números negativos en los reales")
    
    estimacion = numero
    precision = 1e-6
    
    while True:
        siguiente_estimacion = 0.5 * (estimacion + numero / estimacion)
        if abs(siguiente_estimacion - estimacion) < precision:
            return siguiente_estimacion
        estimacion = siguiente_estimacion

try:
    numero = float(input("Ingrese un número para calcular su raíz cuadrada: "))
    resultado = calcular_raiz_cuadrada(numero)
    print(f"La raíz cuadrada de {numero} es aproximadamente {resultado:.6f}")
except ValueError as e:
    print("Error:", e)
except Exception as e:
    print("Ocurrió un error:", e)