#Algortimo para conocer el capital total acumulado 
#al final del periodo de tiempo especificado

def interes_simple(capital, tasa, tiempo):
    return capital * (tasa / 100) * tiempo

capital = float(input("Escriba el capital a depositar(dolares): "))
tasa = float(input("Escriba la tasa propuesta: "))
duracion_semanas = int(input("Duracion del deposito en semanas: "))

interes = interes_simple(capital, tasa, duracion_semanas)
monto_final = capital + interes
print(f"El capital acumlado a devolver es de: {monto_final:.2f} dolares.")