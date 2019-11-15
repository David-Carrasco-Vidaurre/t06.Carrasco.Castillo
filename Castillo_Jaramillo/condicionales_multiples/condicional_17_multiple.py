import os

#Calcular energia potencial gravitatoria de un cuerpo

#Declaracion de variables
masa,gravedad,altura= 0,0,0
energia_potencial_gravitatoria=0

#input
masa= int(os.sys.argv[1])
gravedad= int(os.sys.argv[2])
altura= int(os.sys.argv[3])

#procesing
energia_potencial_gravitatoria= (masa*gravedad*altura)

#output
#Si la energia supera 160 joules mostrar "Mucha energia"
if (energia_potencial_gravitatoria >  160):
    print("Mucha energia")

#Si la energia no supera 70 joules mostrar "Energia insuficiente"
if (energia_potencial_gravitatoria <  70):
    print("Energia insuficiente")

#Si la energia esta entre los 71 y 159 joules mostrar "Energia exacta"
if (71 < energia_potencial_gravitatoria <  159):
    print("Energia exacta")

#fin_if

