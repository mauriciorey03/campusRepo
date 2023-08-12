# archivo=input("Ingrese el nombre")
nombre=("Datos.txt")

archivoLectura= open(nombre, "r+")

unaLinea=archivoLectura.readline()
linea=""
while unaLinea:
    listaPalabras=unaLinea.replace("\n","").split(",")
    suma=0
    for i in range (1,len(listaPalabras)):
        suma+=int(listaPalabras[i])
    linea+=", ".join(listaPalabras)+" ** "+str(round((suma/i),2))+"\n"
    
    unaLinea=archivoLectura.readline()
archivoLectura.close()

archivoEscritura=open("Destino.txt","w")
archivoEscritura.write(linea)
archivoEscritura.close()

linea.


print("Fin")

# r,
# w,
# a,

# readline()
# read()

# tell()
# write()
# close()