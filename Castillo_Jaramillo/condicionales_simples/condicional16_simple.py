import os

#Calcular el trabajo que realiza un cuerpo

#Declaracion de variables
fuerza,distancia= 0,0
trabajo=0

#input
fuerza= int(os.sys.argv[1])
distancia= int(os.sys.argv[2])

#procesing
trabajo= (fuerza*distancia)

#output
#Si el trabajo supera los 200 joules mostrar "Super trabajo"
if (trabajo >  200):
    print("Super trabajo")
#fin_if

