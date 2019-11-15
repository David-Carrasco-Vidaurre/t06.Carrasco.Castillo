import os

#Calcular el volumen del prisma

#Declaracion de variables
area_base,altura= 0,0
volumen= 0

#Input
area_base= int(os.sys.argv[1])
altura= int(os.sys.argv[2])

#procesing
volumen= (area_base*altura)

#output
#Si el area supera los 100 metros cubicos mostrar "Extenso volumen"
if (volumen >  100):
    print("Extenso volumen")

#Si el area no supera los 100 metros cubicos mostrar "Pequeño volumen"
if (volumen < 100):
    print("Pequeño volumen")

#fin_if

