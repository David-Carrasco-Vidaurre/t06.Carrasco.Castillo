import os

# Calcular el promedio de 3 notas de un estudiante.

#Declaración de variables
nota1,nota2,nota3,= 0,0,0
promedio= 0

#input
nota1 = int(os.sys.argv[1])
nota2 = int(os.sys.argv[2])
nota3 = int(os.sys.argv[3])

#procesing
promedio= ((nota1 + nota2 + nota3 )//3)

#output
# Si el promedio supera 16 puntos mostrar "Aprobado"
if (promedio > 16):
    print ("Aprobado")

# Si el promedio no supera 16 puntos mostrar "Necesitas estudiar"
if (promedio < 16):
    print ("Necesitas estudiar")
#fin_if
