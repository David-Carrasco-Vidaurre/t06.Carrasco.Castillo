import os

#Calcular el area del rombo

#Declaracion de variables
diagonal_menor,diagonal_mayor= 0,0
area=0.0,0.0,0.0

#input
diagonal_menor= float(os.sys.argv[1])
diagonal_mayor= float(os.sys.argv[2])

#procesing
area= (diagonal_menor*diagonal_mayor)/2

#output
#Si el area supera los 100 metros cuadrados mostrar "Gran rombo"
if (area >  100):
    print("Gran rombo")

#Si el area no supera los 100 metros cuadrados mostrar "Pequeño rombo"
if (area <  100):
    print("Pequeño rombo")

#fin_if
