#Empresas ={personas[Mauricio={'identificación':0, 'nombre':0, 'edad':0, 'eps':0}, Nicolas={'identificación':0, 'nombre':0, 'edad':0, 'eps':0}, Angie={'identificación':0, 'nombre':0, 'edad':0, 'eps':0}] }
import os
def poblarIniciales(empleados):
    empleados.append({
        "documento": 1,
        "nombre": "Howard",
        "edad": 25,
        "eps": "Sura"
    })
    empleados.append({
        "documento": 2,
        "nombre": "Nahomi",
        "edad": 33,
        "eps": "Solsalud"
    })
    empleados.append({
        "documento": 3,
        "nombre": "Sarita",
        "edad": 21,
        "eps": "SinergiaSalud"
    })
    empleados.append({
        "documento": 4,
        "nombre": "Juliana",
        "edad": 17,
        "eps": "La EPS de SUBIDA"
    })
    

def validarInput(mensaje):
    data = input(mensaje)
    while(data.strip() == ''):
        print("\nIngrese algún dato\n")
        data = input(mensaje)
    return data

def validaDocumento(id, empleados):
    for i in range(len (empleados)):
        if (empleados[i]['documento'] == id):
            return True
    return False
   
def ingresarDatos():
    os.system('clear')

    documento = validarInput("Digite el Documento: ")
    while(validaDocumento(documento,empleados)):
        print("\nEl documento ya existe\n")
        documento = validarInput("Digite el Documento: ")
        
    nombre = validarInput("Digite el Nombre: ")
    edad = validarInput("Digite el Edad: ")
    eps = validarInput("Digite el EPS: ")
   
    empleados.append({
        "documento": documento,
        "nombre": nombre,
        "edad": edad,
        "eps": eps
    })

  

def eliminarRegistro():
    os.system('clear')
    
    doc = input('Ingrese el documento que desea eliminar')

    for i in range(len(empleados)):
        if(empleados[i]['documento'] == doc):
            empl = empleados.pop(i)
            return print('\nSe ha eliminado el registro', empl, '\n')

    return print('\nNo existe el registro con ese documento\n')
   
def reportarListado():
    os.system('clear')
    for j in empleados:
        print(f"El nombre {j['nombre']}")

def menu():
    seguir = True
    while seguir:
        print("Selecciona la opción que desee")
        print("\t1) Ingresar un nuevo registro")
        print("\t2) Eliminar un registro")
        print("\t3) Mostrar listado total")
        print("\t4) Buscar y mostrar un registro")  #****
        print("\t5) Actualizar un registro")  #****
        print("\t6) Salir del Programa")  #****


        opcion = int(input('opcion -> '))

        if(opcion == 6):
            seguir = False
            return print('\nFin del programa\n')

        if(opcion < 1 or opcion > 6):
            return print('\nEl número debe ser entre 0 y 6\n')

        switch = { 1: ingresarDatos, 2: eliminarRegistro, 3: reportarListado }

        switch[opcion]()
empleados = []
poblarIniciales(empleados)
menu()