import os
#declaracion de variables
nombre, años, fecha, hora, luga="",0,"","",""
#input
nombre=os.sys.argv[1]
años=int(os.sys.argv[2])
fecha=os.sys.argv[3]
hora=os.sys.argv[4]
lugar=os.sys.argv[5]

#processing
verificador=(años>14)
#output
print("☺ Te invito a mi fiesta de cumpleaños infantil")
print("De:" , nombre)
print("Cumple:" ,años , "años")
print("Fecha:", fecha)
print("Hora:", hora)
print("Lugar:", lugar)
print("NO FALTES")

#si es mayor de 15
if(verificador):
    print("Usted esta muy grande para fiesta infantil")
#fin_if
