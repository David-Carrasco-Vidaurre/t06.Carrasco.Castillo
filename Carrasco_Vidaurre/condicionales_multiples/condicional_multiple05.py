import os
#declaracion de variables
nombre,nro_celular, carrera, fecha, modalidad, verificador, matricula="", 0,"", "","",False, 0.0
#input
nombre=os.sys.argv[1]
nro_celular=int(os.sys.argv[2])
carrera=os.sys.argv[3]
fecha=os.sys.argv[4]
modalidad=os.sys.argv[5]
matricula=float(os.sys.argv[6])

#processing
monto_matricula=matricula
verificador=(matricula>=200)

#output
print("Universidad Nacional Pedro Ruiz Gallo")
print("Facultad de Ciencias Fisicas y Matematicas")
print("#Constancia de Matricula")
print("Nombre:", nombre)
print("Numero de telefono:", nro_celular)
print("Carrera Profesional:", carrera)
print("Fecha:",fecha)
print("Modalidad de ingreso:", modalidad)
print("La matricula:", matricula)

#para los estudiantes
if(verificador):
    print("Bienvenidos Cachimbo")
if(matricula<50):
    print("bienvenido a clases")
if(matricula>=50 and matricula<200):
    print("Bienvenido")
#fin_if
