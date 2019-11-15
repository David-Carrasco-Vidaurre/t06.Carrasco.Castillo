import os

# Dado la talla y peso de unos niños de 10 años. Calcular su IMC

#Declaracion de variables
talla, peso = 0.0,0
IMC= 0.0

#input
talla= float(os.sys.argv[1])
peso= int(os.sys.argv[2])

#procesing
IMC= (( peso )//talla * talla)

#output
# Si el IMC no supera los 78.8  mostrar "Niño sano"
if (IMC < 78.8):
    print ("Niño sano")
#fin_if
