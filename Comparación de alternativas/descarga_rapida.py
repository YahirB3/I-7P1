archivo = 5000
vel_A = 40
vel_B = 80

tiempo_A = archivo / vel_A
tiempo_B = archivo / vel_B  

print(tiempo_A)
print(tiempo_B)

if tiempo_A < tiempo_B:
    print("Debe descargar con la conexion A")
else:
    print("Debe descargar con la conexion B")