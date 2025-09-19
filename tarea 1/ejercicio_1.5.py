foco_viejo = 100 # Watts
foco_nuevo = 60 # Watts
foco_LED = 15 # Watts
horas = 5 
dias = 30
gasto_viejo = foco_viejo * horas
gasto_nuevo = foco_nuevo * horas
gasto_LED = foco_LED * horas
print("Consumo con foco viejo:", gasto_viejo, "Wh")
print("Consumo con foco nuevo:", gasto_nuevo, "Wh")
print("Consumo con foco LED:", gasto_LED, "Wh")
print("Ahorro:", gasto_viejo - gasto_nuevo, "Wh por dia")
print("Ahorro al mes:", (gasto_viejo - gasto_nuevo) * dias, "Wh")
print("Ahorro:", gasto_viejo - gasto_LED, "Wh por dia")
print("Ahorro al mes:", (gasto_viejo - gasto_LED) * dias, "Wh")