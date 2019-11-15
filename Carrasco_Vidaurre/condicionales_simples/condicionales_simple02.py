import os
#declaracion de variables
cliente, nro_dni, nro_ruc, nombre_libro1, nombre_libro2, precio_libro1, precio_libro2, total_pagar="", 0,0,"","",0.0,0.0,0.0
verificador=False

#input
cliente=os.sys.argv[1]
nro_dni=int(os.sys.argv[2])
nro_ruc=int(os.sys.argv[3])
nombre_libro1=os.sys.argv[4]
nombre_libro2=os.sys.argv[5]
precio_libro1=float(os.sys.argv[6])
precio_libro2=float(os.sys.argv[7])

#procesing
total_pagar=(precio_libro1+precio_libro2)
verificador=(total_pagar>=40)

#output
print("#########################")
print("#  Libreria Bazar: El Diamante")
print("#Cliente:", cliente)
print("#Nro de DNI:", nro_dni)
print("#Nro de Ruc:",nro_ruc)
print("#Libro:", nombre_libro1 ,"               Precio:", precio_libro1)
print("#Libro:", nombre_libro2 ,"              Precio:", precio_libro2)

print("Total a pagar:", total_pagar)

#Si el total a pagar supera el monto de 60 soles
if(verificador):
    print("Felicidades recibe un descuento del 10%")
#fin_if
