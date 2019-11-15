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

#Si el area no supera los 50 metros cuadrados mostrar "Pequeño rombo"
if (area <  50):
    print("Pequeño rombo")

#Si el area esta entre los 51 y 99  metros cuadrados mostrar "Mediano rombo"
if (51 < area < 99):
    print("Mediano rombo")

#fin_if
