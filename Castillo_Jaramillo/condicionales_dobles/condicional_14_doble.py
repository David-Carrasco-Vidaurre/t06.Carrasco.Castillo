import os

#Calcular el area del trapecio

#Declaracion de variables
base_menor,base_mayor,altura= 0,0,0
area=0

#input
base_menor= int(os.sys.argv[1])
base_mayor= int(os.sys.argv[2])
altura= int(os.sys.argv[3])

#procesing
area= (base_menor+base_mayor)*altura//2


#output
#Si el area supera los 150 metros cuadrados mostrar "Gran trapecio"
if (area >  150):
    print("Gran trapecio")

#Si el area no supera los 150 metros cuadrados mostrar "Pequeño trapecio"
if (area <  150):
    print("Pequeño trapecio")

#fin_if

