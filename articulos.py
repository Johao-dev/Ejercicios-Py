#Algoritmo factura de compra

articulo = input("¿Cúal es el articulo que desea comprar?: ")
precio_venta = int(input("Precio: "))
unidades = int(input("Ingrese unidades: "))

precio_venta *= unidades
precio_bruto = precio_venta + (precio_venta*0.15)

if precio_bruto > 1000:
    descuento = precio_bruto * (5/100)
    precio_bruto -= descuento

print(f"Total a pagar: {precio_bruto:.2f}")