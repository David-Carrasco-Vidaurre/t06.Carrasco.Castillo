import os

#Calcular la dstancia de un vehiculo

#Declaracion de variables
velocidad,tiempo= 0,0
distancia= 0

#input
velocidad= int(os.sys.argv[1])
tiempo= int(os.sys.argv[2])

#procesing
distancia= int(velocidad*tiempo)

#output
#Si la distancia supera los 200 metros  mostrar "Distancia larga"
if (distancia >  200):
    print("Distancia larga")

#Si la distancia no supera los 70 metros  mostrar "Distancia corta"
if (distancia <  70):
    print("Distancia corta")

#Si la distancia esta entre los 69 y 199 metros  mostrar "Distancia normal"
if (71 < distancia <  199):
    print("Distancia normal")

#fin_if



