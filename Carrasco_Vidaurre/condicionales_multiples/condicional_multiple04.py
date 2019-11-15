import os
#declaracion de variables
diagonal_menor, diagonal_mayor, altura, verificador, area=0.0,0.0,0.0,False, 0.0

#input
diagonal_mayor=float(os.sys.argv[1])
diagonal_menor=float(os.sys.argv[2])
altura=float(os.sys.argv[3])

#processing
area=float(((diagonal_mayor+diagonal_menor)*altura)//2)
verificador=(area>=100)

#output
print("Area de un Rombo")
print("Diagonal Mayor:", diagonal_mayor)
print("Diagonal Menor:", diagonal_menor)
print("Altura:", altura)
print("Area:", area)

#si el area es supera los 20m cuadrados
if(verificador):
    print("Superficie muy grande")
if(area>=40 and area<100 ):
    print("Superficie intermedio")
if(area<40):
    print("Superficie normal")

#fin_if
