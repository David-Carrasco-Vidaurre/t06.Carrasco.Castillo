import os
#declaracion de variables
nombre, apellidos, nombre_usuario,  correo_electronico, genero, edad="","","","","",0
verificador=False

#input
nombre=os.sys.argv[1]
apellidos=os.sys.argv[2]
nombre_usuario=os.sys.argv[3]
edad=int(os.sys.argv[4])
correo_electronico=os.sys.argv[5]
genero=os.sys.argv[6]
verificador=(edad<15)

 #output
print("Registrar cuenta en Facebook")
print("Nombre:", nombre)
print("Apellidos:", apellidos)
print("Nombre de usuario:", nombre_usuario)
print("Correo electronico:", correo_electronico)
print("Genero:", genero)
print("Edad:",edad)

#Si el usuario es menor de 15
if(verificador):
    print("Usted no tiene la edad requerida")
if(edad>=18):
    print("Bienvenido")
if(edad>=15 and edad<18):
    print("Cuenta registrada")
#fin_if
