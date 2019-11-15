import os
#declaracion de variables
gasto_semana1,gasto_semana2, gasto_semana3, gasto_semana4, gasto_mesual=0.0,0.0,0.0,0.0,0.0
verificador=False


#input
gasto_semana1=float(os.sys.argv[1])
gasto_semana2=float(os.sys.argv[2])
gasto_semana3=float(os.sys.argv[3])
gasto_semana4=float(os.sys.argv[4])

#processing
gasto_mesual=(gasto_semana1+gasto_semana2+gasto_semana3+gasto_semana4)
verificador=(gasto_mesual>=50)

#outpu
print("##########################################")
print("Gasto semana 1:", gasto_semana1)
print("Gasto semana 2:", gasto_semana2)
print("Gasto semana 3:",gasto_semana3)
print("Gasto semana 4:",gasto_semana4)
print("Gasto mensual:",gasto_mesual)

#si pasa los 50soles
if(verificador):
    print("Ud Esta Excedido")
if(gasto_mesual<=30):
    print("Gasto Recomendado")

if(gasto_mesual>30 and gasto_mesual<50):
    print("Gasto medio")


#fin_if
