#Un estudiante tiene 3 rutas para llegar a la escuela

camino1 = 12
camino2 = 18
camino3 = 10

if camino1 < camino2 and camino1 < camino3:
    print("El estudiante debe tomar el camino 1")
elif camino2 < camino1 and camino2 < camino3:
    print("El estudiante debe tomar el camino 2")
else:
    print("El estudiante debe tomar el camino 3")