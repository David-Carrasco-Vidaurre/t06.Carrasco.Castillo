import os

# Dado la talla y peso de unos niños . Calcular su IMC

#Declaración de variables
talla, peso = 0.0,0
IMC= 0.0

#input
talla= float(os.sys.argv[1])
peso= int(os.sys.argv[2])

#procesing
IMC= (( peso )//talla * talla)


#output
# Si el IMC no supera los 60.8  mostrar "Niño con anorexia"
if (IMC < 60.8):
    print ("Niño con anorexia")

# Si el IMC supera los 75.9  mostrar "Niño con obesidad"
if (IMC > 75.9):
    print ("Niño con obesidad")

# Si el IMC esta entre 60.9 y 75.8 mostrar "Niño normal"
if (60.9 < IMC < 75.8):
    print ("Niño normal")
#fin_if
