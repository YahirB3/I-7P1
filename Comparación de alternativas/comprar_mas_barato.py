#En el mercado hay 3 puestos que venden manzanas:
# Escribe el código que compare los precios y muestre el ahorro
puestoA = 35   
puestoB = 30 
puestoC = 28

descuentoB = puestoB * 0.10
ahorroB = puestoB - descuentoB

if puestoA < puestoB and puestoA < puestoC:
    print("Debe comprar en el puesto A")
elif ahorroB < puestoA and ahorroB < puestoC:
    print("Debe comprar en el puesto B")
else:
    print("Debe comprar en el puesto C")
