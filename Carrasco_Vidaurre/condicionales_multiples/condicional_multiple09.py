import os
#declaracion de variables
velocidad_inicial, tiempo_segundos, aceleracion, distancia=0.0,0.0,0.0,0.0
verificador=False
#input
velocidad_inicial=float(os.sys.argv[1])
tiempo_segundos=float(os.sys.argv[2])
aceleracion=float(os.sys.argv[3])

#procesing
distancia=((velocidad_inicial*tiempo_segundos)+((aceleracion*tiempo_segundos+tiempo_segundos)//2))
verificador=(distancia>1000)

#output
print("# Formula de la distancia")
print("Velocidad inicial:", velocidad_inicial)
print("Tiempo:", tiempo_segundos)
print("Aceleracion:", aceleracion)
print("Distancia", distancia)

#Distancia excedida
if(verificador):
    print("Distancia Excedida")
if(distancia<=500):
    print("Distancia normal")
if(distancia>500 and distancia<=1000):
    print("Distancia Levemente execida")
#fin_if
