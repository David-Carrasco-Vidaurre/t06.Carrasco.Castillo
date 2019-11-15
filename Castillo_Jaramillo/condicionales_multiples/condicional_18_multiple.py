import os

#Calcular la densidad de un cuerpo

#Declaracion de variables
masa,volumen = 0,0
densidad= 0

#input
masa= int(os.sys.argv[1])
volumen= int(os.sys.argv[2])

#procesing
densidad= (masa//volumen)

#output
#Si la densidad del cuerpo supera los 8 metros cubicos mostrar "Alta densidad"
if (densidad >  8):
    print("Alta densidad")

#Si la densidad del cuerpo no supera los 4 metros cubicos mostrar "Baja densidad"
if (densidad <  4):
    print("Baja densidad")

#Si la densidad del cuerpo esta entre los 5 y 7 metros cubicos mostrar "Densidad normal"
if (5 < densidad < 7):
    print("Densidad normal")
#fin_if


