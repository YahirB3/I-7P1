#Calcula cuánto tiempo puede usarse con cada app y elige la más eficiente.
bateria = 5000
app1 = 400
app2 = 250
app3 = 150

tiempo_app1 = bateria / app1
tiempo_app2 = bateria / app2
tiempo_app3 = bateria / app3

print(tiempo_app1)
print(tiempo_app2)
print(tiempo_app3)
if tiempo_app1 > tiempo_app2 and tiempo_app1 > tiempo_app3:
    print("La app 1 es mas eficiente.")
elif tiempo_app2 > tiempo_app1 and tiempo_app2 > tiempo_app3:
    print("La app 2 es mas eficiente.")
else:
    print("La app 3 es mas eficiente.")