import os

#Calcular la potencia de un motor

#Declaracion de variables
trabajo,tiempo= 0,0
potencia=0.0

#input
trabajo= int(os.sys.argv[1])
tiempo= int(os.sys.argv[2])

#procesing
potencia= (trabajo//tiempo)

#output
#Si la potencia es menor a 50 watts mostrar "Potencia minima"
if (potencia <  150):
    print("Potencia minima")
#fin_if

