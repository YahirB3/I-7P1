camino1 = 10 # minutos
camino2 = 15 # minutos
camino3 = 8 # minutos
if camino1 < camino2 and camino1 < camino3:
    print("El camino 1 es el mas corto")
    print("Tiempo:", camino1, "minutos")
elif camino2 < camino1 and camino2 < camino3:
    print("El camino 2 es el mas corto")
    print("Tiempo:", camino2, "minutos")
elif camino3 < camino1 and camino3 < camino2:
    print("El camino 3 es el mas corto")
    print("Tiempo:", camino3, "minutos")
