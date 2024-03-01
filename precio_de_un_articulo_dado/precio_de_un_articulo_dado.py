import math

#programa para calcular el precio de venta 

#input 
PRECIO_COSTO =int(input("ingrese el valor del producto adquerido:_ "))

#processing

if PRECIO_COSTO < 3000:
    GANANCIA = PRECIO_COSTO * 0.15
elif PRECIO_COSTO > 6000:
    GANANCIA = PRECIO_COSTO * 0.25
else:
    GANANCIA = 500

PRECIO_VENTA = (GANANCIA + PRECIO_COSTO)

# output
print( "el producto adquerido se debe vender a",PRECIO_VENTA,)