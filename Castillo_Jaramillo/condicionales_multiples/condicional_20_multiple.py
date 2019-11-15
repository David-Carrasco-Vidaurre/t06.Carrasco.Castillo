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
if (potencia <  10):
    print("Potencia minima")

#Si la potencia es mayor a 50 watts mostrar "Potencia maxima"
if (potencia >  50):
    print("Potencia maxima")

#Si la potencia esta entre los 11 y 49 watts mostrar "Potencia normal"
if (11 < potencia <  49):
    print("Potencia normal")
#fin_if

