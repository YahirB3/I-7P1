#Calcula el consumo diario de cada uno y el ahorro.
viejo = 100
nuevo = 20
horas = 6
# Calcula consumos y ahorro
consumo_viejo = (viejo * horas) 
consumo_nuevo = (nuevo * horas) 
ahorro = consumo_viejo - consumo_nuevo
print(consumo_viejo)
print(consumo_nuevo)
print("se tiene un ahorro de", ahorro)

mensual_viejo = consumo_viejo * 30
mensual_nuevo = consumo_nuevo * 30

ahorro_mensual = mensual_viejo - mensual_nuevo
print("se tiene un ahorro mensual de", ahorro_mensual)
