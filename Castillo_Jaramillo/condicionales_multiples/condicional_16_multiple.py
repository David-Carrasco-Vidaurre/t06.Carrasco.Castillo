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
#Si el trabajo supera los 200 joules mostrar "Excelente trabajo"
if (trabajo >  200):
    print("Excelente trabajo")

#Si el trabajo no supera los 100 joules mostrar "Deficiente trabajo"
if (trabajo <  100):
    print ("Deficiente trabajo")

#Si el trabajo esta entre los 101 y 199 joules mostrar "Eficiente trabajo"
if (101 < trabajo <  199):
    print ("Eficiente trabajo")

#fin_if

