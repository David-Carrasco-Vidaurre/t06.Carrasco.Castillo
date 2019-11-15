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
#Si la distancia supera los 150 metros  mostrar "Distancia larga"
if (distancia >  150):
    print("Distancia larga")

#Si la distancia no supera los 150 metros  mostrar "Distancia corta"
if (distancia <  150):
    print("Distancia corta")

#fin_if



