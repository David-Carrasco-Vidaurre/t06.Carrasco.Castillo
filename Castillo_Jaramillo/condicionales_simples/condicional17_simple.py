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
#Si la energia supera 150 joules mostrar "Mucha energia"
if (energia_potencial_gravitatoria >  150):
    print("Mucha energia")
#fin_if


