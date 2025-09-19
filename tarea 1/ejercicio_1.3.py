tienda_A = 200 # pesos
tienda_B = 180 # pesos
tienda_C = 150 # pesos
if tienda_A < tienda_B and tienda_A < tienda_C:
    print("Conviene comprar en la Tienda A")
    print("Ahorro:", tienda_B - tienda_A, "pesos")
elif tienda_B < tienda_A and tienda_B < tienda_C:
    print("Conviene comprar en la Tienda B")
    print("Ahorro:", tienda_A - tienda_B, "pesos")
else:
    print("Conviene comprar en la Tienda C")
    print("Ahorro:", tienda_B - tienda_C, "pesos")