def msgError(msg):
    print(msg)
    input("Presione cualquier tecla para continuar ...")

def leerStr(msg):
    while True:
        try:
            n = input(msg)
            if n == None or n.strip() == "":
                print("Error, por favor ingrese los datos.")
                continue
            return n
        except Exception as e:
            print("Ha sucedido un Error: ", e)
            continue

def leerNota(msg):
    while True:
        try:
            num = float(input(msg))
            if num < 0:
                print("El numero no puede ser 0")
                input("Presione cualquier tecla para continuar ...")
                continue
            elif num > 5:
                print("El numero no puede ser mayor a 5")
                input("Presione cualquier tecla para continuar ...")
                continue
            break
        except ValueError:
            print("Número inválido.")
            input("Presione cualquier tecla para continuar ...")
    return num

# estudiantes=[
#     'est1':
#         {'código':0, 'nombre':0, 'notas':[nota1,nota2,nota3], 'definitiva':0}
# ]

# print(estudiantes["est1"])
estudiantes=[]

def agregarEstudiante(dicEst):
    print("\n\n*** 1. Agregar estudiante ***\n")
    
    id = leerStr("Id del estudiante: ")
    nom = leerStr("Nombre del estudiante: ")
    nota1 = leerNota("Nota 1: ")
    nota2 = leerNota("Nota 2: ")
    nota3 = leerNota("Nota 3: ")
    notas=[nota1,nota2,nota3]
    datest ={"codigo":id, "nombre":nom, 'notas':notas}
    dicEst.append(datest) 
    
    # print(dicEst)
    # input()

def buscarEstudiante(dicEst, id):
    for i in range(len(dicEst)):
        if id == dicEst[i]["codigo"]:
            return i
    return None

def buscarEst(dicEst):
    print("\n\n*** 2. Buscar estudiante ***\n")
    
    id = leerStr("Id del estudiante: ")
    pos = buscarEstudiante(dicEst, id)
    if pos != None:
        print("\nNombre:", dicEst[pos]["nombre"])
        print("Notas:", dicEst[pos]['notas'][0], dicEst[pos]['notas'][1], dicEst[pos]['notas'][2])

    else:
        print("\nEl estudiante no ha sido ingresado")
        
    input("Presione cualquier tecla para continuar ...")


def modiEst(dicEst):
    print("\n\n*** 3. Modificar estudiante ***\n")
    
    id = leerStr("Id del estudiante: ")
    pos = buscarEstudiante(dicEst, id)
    if pos != None:
        print("Va a modificar la información de: ", dicEst[pos]["codigo"])
        print("Cual valor desea modificar:\n\
            \t1.Nombre\n\
            \t2.Nota 1\n\
            \t3.Nota 2\n\
            \t4.Nota 3\n\
            o presione cualquier tecla para cancelar")
        newMod=int(input("Seleccione una opc: "))
        if newMod==1:
            name=input("Ingrese el nuevo nombre: ")
            dicEst[pos]["nombre"]=name
            print("Se modificó el nuevo nombre: ", name)
        elif newMod==2:
            nota1=input("Ingrese la nueva nota 1: ")
            dicEst[pos]['notas'][0]=nota1
            print("Se modificó la nota 1: ", nota1)
        elif newMod==3:
            nota2=input("Ingrese nueva la nota 2: ")
            dicEst[pos]['notas'][1]=nota2
            print("Se modificó la nota 2: ", nota2)
        elif newMod==3:
            nota3=input("Ingrese nueva la nota 3: ")
            dicEst[pos]['notas'][2]=nota3
            print("Se modificó la nota 3: ", nota3)
        else:
            print("Se cancelo la modificación.")
    else:
        print("\nEl código no existe.")
    input("Presione cualquier tecla para continuar ...")

def borrarEstudiante(dicEst):
    print("\n\n*** 4. Borar estudiante ***\n")
    id = leerStr("Ingrese el id del estudiante que desea eliminar: ")
    pos = buscarEstudiante(dicEst, id)
    if pos != None:
        print("\nNombre:", dicEst[pos]["nombre"])
        si=input("Está seguro que desea eliminarlo? (si para confirmar)")
        if si=="si" or si=="SI" or si=="Si":
            del dicEst[pos]
            print("El estudiante se eliminó satisfactoriamente.")
        else:
            print("Se canceló.")
    else:
        print("\nEl estudiante no existe ha sido ingresado")
        
    input("Presione cualquier tecla para continuar ...")

def listarEstudiantes(dicEst):
    print("\n\n*** 6. Listar estudiantes ***\n")
    for i in range(0,len(dicEst)):
        print("Estudiante:", (i+1), dicEst[i]["nombre"])
    input("Presione enter para continuar.")


def calcularDef(nota1, nota2, nota3):
    notaFinal=(nota1+nota2+nota3)/3
    return notaFinal

def menu():
    while True:
        try:
            print("\n\n*** CRUD - ESTUDIANTES ***")
            print("\tMENU")
            print("# 1. Agregar un nuevo registro\n\
# 2. Buscar un Estudiante\n\
# 3. Actualizar datos del Estudiante.\n\
# 4. Borrar un estudiante.\n\
# 5. Calcular notas definitivas\n\
# 6. Listar estudiantes con notas definitivas y ver promedio general\n")
            op = int(input("\t>> Escoja una opción (1-6)?"))
            if op < 1 or op > 6:
                msgError("Error. Opción Inválida (de 1 a 6).")
                continue
            return op
        except ValueError:
            msgError("Error. Opción Inválida (de 1 a 6).")
            continue
        
def main():
    dicEst = []
    while True:
        op = menu()
        if op == 1:
            agregarEstudiante(dicEst)
        elif op == 2:
            buscarEst(dicEst)
        elif op == 3:
            modiEst(dicEst)
        elif op == 4:
            borrarEstudiante(dicEst)
        elif op == 5:
            calcularDef(dicEst)
        elif op == 6:
            listarEstudiantes(dicEst)
        # colocar otras opciones
        else:
            print("\n", "Gracias por usar el programa... Adios...".center(80))
            break
    

# Programa Principal
main()