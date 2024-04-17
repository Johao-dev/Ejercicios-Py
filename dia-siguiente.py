from datetime import datetime, timedelta

def obtener_fecha_siguiente():
    fecha_str = input("Ingresa la fecha (formato DIA, MES, AÑO): ")
    
    try:
        # Parseamos la fecha introducida como una cadena al formato de fecha
        fecha = datetime.strptime(fecha_str, "%d, %m, %Y")
        
        # Añadimos un día a la fecha utilizando timedelta
        fecha_siguiente = fecha + timedelta(days=1)
        
        # Imprimimos la fecha del día siguiente
        print("La fecha del día siguiente es:", fecha_siguiente.strftime("%d/%m/%Y"))
    except ValueError:
        print("Formato de fecha incorrecto. Asegúrate de ingresar la fecha en el formato DIA, MES, AÑO (ejemplo: 01, 01, 2023)")

# Llamamos a la función para obtener la fecha del día siguiente
obtener_fecha_siguiente()
