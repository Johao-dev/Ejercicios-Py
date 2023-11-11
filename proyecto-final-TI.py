#Proyecto final de TI

#Diccionario de los precios de los items

precios = {
    "Desayuno": {
        "Cafe": 4.50,
        "Chocolate": 5.00,
        "Jugo de fresas": 9.00,
        "Jugo de papaya": 8.00,
        "Pan con pollo": 7.00,
        "Pan con jamon": 7.00,
        "Pan con tortilla": 7.00
    },
    "Almuerzo": {
        "Arroz con pollo": 15.00,
        "Lomo saltado": 20.00,
        "Ensalada rusa": 12.00
    },
    "Cena": {
        "Pizza expres": 9.50,
        "Ensalada campera": 7.50,
        "Gazpacho": 6.00,
        "Caldo de gallna": 6.00,
        "Pollo al horno": 5.00,
        "Menestron": 4.00
        }
    }
#Variable para almacenar el total, IGV y subtotal
total = 0
igv = 0.18
subtotal = 0
#Bucle para mostrar el menú principal
continuar = True

while (continuar == True):
    print("\n\n\n|==================================|")
    print("|          RESTAURANTE PUNTA AZUL  S.A   |")
    print("|                     MENU               |")
    print("|========================================|")
    print("|   A|  DESAYUNO                         |")
    print("|   B|  ALMUERZO                         |")
    print("|   C|  CENA                             |")
    print("|   D|============ SALIR ================|")
    print("|========================================|")

    opcion = input("\nElija una opcion: ")

    if (opcion == "A"):
        print("\n\n\n|              DESAYUNO               |")
        print("|===========================================|")
        print("|   A  |Cafe                       |S/4.50  |")
        print("|   B  |Chocolate                  |S/5.00  |")
        print("|   C  |Jugo de fresas             |S/9.00  |")
        print("|   D  |Jugo de papaya             |S/8.00  |")
        print("|   E  |Pan con pollo              |S/7.00  |")
        print("|   F  |Pan con jamón              |S/7.00  |")
        print("|   G  |Pan con tortilla           |S/7.00  |")
        print("|   J  |=============== SALIR ==============|")

        opcion_desayuno = input("\nElija su desayuno: ")

        if (opcion_desayuno == "A"):
            subtotal += precios["Desayuno"]["Cafe"]
        elif opcion_desayuno == "B":
            subtotal += precios["Desayuno"]["Chocolate"]
        elif opcion_desayuno == "C":
           subtotal += precios["Desayuno"]["Jugo de fresas"]
        elif opcion_desayuno == "D":
            subtotal += precios["Desayuno"]["Jugo de papaya"]
        elif opcion_desayuno == "E":
            subtotal += precios["Desayuno"]["Pan con pollo"]
        elif opcion_desayuno == "F":
            subtotal += precios["Desayuno"]["Pan con jamon"]
        elif opcion_desayuno == "G":
            subtotal += precios["Desayuno"]["Pan con tortilla"]

    elif opcion ==  "B":
        print("\n\n\n|               ALMUERZO              |")
        print("|===========================================|")
        print("|   A  |Arroz con pollo            |S/15.00 |")
        print("|   B  |Lomo saltado               |S/20.00 |")
        print("|   C  |Ensalada rusa              |S/12.00 |")

        opcion_almuerzo = input("\nElija su almuerzo: ")

        if (opcion_almuerzo == "A"):
            subtotal += precios["Almuerzo"]["Arroz con pollo"]
        elif opcion_almuerzo == "B":
            subtotal += precios["Almuerzo"]["Lomo saltado"]
        elif opcion_almuerzo == "C":
            subtotal += precios["Almuerzo"]["Ensalada rusa"]

    elif opcion == "C":
        print("\n\n\n|              CENA                   |")
        print("|===========================================|")
        print("|   A  |Pizza expres                |S/9.50 |") 
        print("|   B  |Ensalada campera            |S/7.50 |")
        print("|   C  |Gazpacho                    |S/6.00 |")
        print("|   D  |Caldo de gallina            |S/6.00 |")
        print("|   E  |Pollo al horno              |S/5.00 |")
        print("|   F  |Menestron                   |S/4.00 |")
        print("|   G  |============= SALIR ================|")
        print("|===========================================|")

        opcion_cena = input("\nElija su cena: ")

        if (opcion_cena == "A"):
            subtotal += precios["Cena"]["Pizza expres"]
        elif opcion_cena == "B":
            subtotal += precios["Cena"]["Ensalada campera"]
        elif opcion_cena == "C":
            subtotal += precios["Cena"]["Gazpacho"]
        elif opcion_cena == "D":
            subtotal += precios["Cena"]["Caldo de gallina"]
        elif opcion_cena == "E":
            subtotal += precios["Cena"]["Pollo al horno"]
        elif opcion_cena == "F":
            subtotal += precios["Cena"]["Menestron"]

    elif opcion == "D":
        continuar = False
        if (subtotal > 0):
            igv = (subtotal * igv)
            total = (subtotal + igv)

            print("\n\n\n|     BOLETA DE VENTAS      |")
            print("|=================================|")
            print("|  Subtotal        : S/{:>9.2f}   |".format(subtotal))
            print("|  Igv             : S/{:>9.2f}   |".format(igv))
            print("|  Total a pagar   : S/{:>9.2f}   |".format(total))
            print("|                                 |")
            print("|    Gracias por su compra        |")
            print("|=================================|\n")
        else:
            print("\nNo se entrego boleta.\n") 

        