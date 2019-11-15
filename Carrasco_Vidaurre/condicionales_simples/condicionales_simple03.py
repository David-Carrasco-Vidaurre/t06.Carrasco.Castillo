import os
#declaracion de variables
total_pagar,cliente, nro_asiento, nro_dni, costo_pasaje, fecha, ruta, verificador= 0.0,"", 0,0,0.0,"", "", False
#input
cliente=os.sys.argv[1]
nro_asiento=int(os.sys.argv[2])
nro_dni=int(os.sys.argv[3])
costo_pasaje=float(os.sys.argv[4])
fecha=os.sys.argv[5]
ruta=os.sys.argv[6]
igv=0.1
#procesign
total_pagar=(costo_pasaje+(costo_pasaje*igv))
verificador=(total_pagar>0)

#output
print("# Empresa de Transporte: Turela" )
print("Cliente:", cliente)
print("Asiento:", nro_asiento)
print("Nro de DNI:", nro_dni)
print("Costo del pasaje", costo_pasaje)
print("Fecha:",fecha)
print("Ruta:", ruta)
print("Total a pagar", total_pagar)

#Cuando el cliente compra pasaje
if(verificador):
    print("Feliz Viaje")
#fin_if
