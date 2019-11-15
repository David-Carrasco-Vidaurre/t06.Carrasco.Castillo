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

#Si el area no supera los 50 metros cubicos mostrar "Pequeño volumen"
if (volumen < 50):
    print("Pequeño volumen")

#Si el area esta entre los 51 y 99 metros cubicos mostrar "Volumen normal"
if (51 < volumen < 99):
    print("Volumen normal")
#fin_if

