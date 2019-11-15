import os
#declaracion de variables
cliente, fruta, cantidad, precio_kg, total="", "",0.0,0.0,0.0
verificador=False

#input
cliente=os.sys.argv[1]
fruta=os.sys.argv[2]
cantidad=float(os.sys.argv[3])
precio_kg=float(os.sys.argv[4])

#procesing
total=(cantidad*precio_kg)
verificador=(total>50)
#output
print("Compra de Fruta")
print("Cliente:" , cliente)
print("Fruta", fruta)
print("Cantidad: ", cantidad, "Kg")
print("Precio por Kg:", precio_kg)
print("Total a pagar:", total)

#Si se excede
if(verificador):
    print("Recibe un bono")
if(total<50 and total>20):
    print("Recibe un descuento del 5% ")
if(total<=20):
    print("Vuelva pronto")
#fin_if
