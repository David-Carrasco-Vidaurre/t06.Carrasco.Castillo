import os
#declaracion de variables
carga01,carga02,constante_electrica,distancia,fuerza_electrica, verificador=0.0,0.0,0,0.0,0.0,False
#input
carga01 =float(os.sys.argv[1])
carga02 =float(os.sys.argv[2])
constante_electrica = 9000000000
distancia =float(os.sys.argv[3])

#procesing
fuerza_electrica= (carga01*carga02 * constante_electrica) // (distancia*distancia)
verificador=(fuerza_electrica>=300000)
#output
print("#Calculadora de Fuerza Electrica")
print ( " carga01 = " , carga01)
print ( " carga02 = " , carga02)
print ( " contante_electrica = " , constante_electrica)
print ( " distancia = " , distancia)
print ( " fuerza_electrica = " , fuerza_electrica)

#si la fuerza es mayor
if(verificador):
    print("Tenga Cuidado")
if(fuerza_electrica<100000):
    print("Fuerza electrica normal")
if(fuerza_electrica>=100000 and fuerza_electrica<300000):
    print("Fuerza electrica Moderada")

#fin_if

