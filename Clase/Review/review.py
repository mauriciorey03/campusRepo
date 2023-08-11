def msgError(msg):
    print(msg)
    input("Presione cualquier tecla para continuar ...")
    
def findEmpl(lstEmpl, id):
    for i in range(len(lstEmpl)):
        if id == lstEmpl[i][0]:
            return i
        
    return None

def buscarEmpleado(lstEmpl):
    print("\n\n*** 3. Buscar empleado - ACME ***\n")
    
    id = leerId("Id del empleado: ")
    pos = findEmpl(lstEmpl, id)
    if pos != None:
        print("\nNombre:", lstEmpl[pos][1])
        print("Horas trabajadas:", lstEmpl[pos][2])
        print(f"Valor Hora: ${lstEmpl[pos][3]:,.0f}")
    else:
        print("\nEl empleado no ha sido ingresado")
        
    input("Presione cualquier tecla para continuar ...")

def eliminaEmpleado(lstEmpl):
    print("\n\n*** 4. Modificar empleado - ACME ***\n")
    id = leerId("Ingrese el id del empleado que desea eliminar: ")
    pos = findEmpl(lstEmpl, id)
    if pos != None:
        print("\nNombre:", lstEmpl[pos][1])
        si=input("Está seguro que desea eliminarlo?")
        if si=="y":
            del lstEmpl[pos]
            print("El empleado se eliminó satisfactoriamente.")
        else:
            print("Se canceló.")
    else:
        print("\nEl empleado no existe ha sido ingresado")
        
    input("Presione cualquier tecla para continuar ...")


def modificarEmpleado(lstEmpl):
    print("\n\n*** 2. Modificar empleado - ACME ***\n")
    
    id = leerId("Id del empleado: ")
    pos = findEmpl(lstEmpl, id)
    if pos != None:
        print("Va a modificar la información de: ", lstEmpl[pos][1])
        print("Cual valor desea modificar:\n\
\t1.Nombre\n\
\t2.Horas trabajadas\n\
\t3.Valor hora\n\
o presione cualquier tecla para cancelar")
        newMod=int(input("Seleccione una opc: "))
        if newMod==1:
            name=input("Ingrese el nuevo nombre: ")
            lstEmpl[pos][1]=name
            print(lstEmpl[pos])
        elif newMod==2:
            hora=input("Ingrese la nueva cantidad de horas: ")
            lstEmpl[pos][2]=hora
            print(lstEmpl[pos])
        elif newMod==3:
            valhora=input("Ingrese el nuevo valor de hora: ")
            lstEmpl[pos][3]=valhora
            print(lstEmpl[pos])
        else:
            print("Se cancelo la modificación.")
    else:
        print("\nEl código no existe.")
        
    input("Presione cualquier tecla para continuar ...")

def listaEmpleado(lstEmpl):
    print("\n\n*** 5. Listar empleados - ACME ***\n")
    for i in range(0,len(lstEmpl)):
        print("Empleado:", (i+1), lstEmpl[i][1])
    input("Presione enter para continuar.")
    

def listaNomina(lstEmpl):
    print("\n\n*** 6. Listar la nómina de un empleado - ACME ***\n")
    id = leerId("Id del empleado: ")
    pos = findEmpl(lstEmpl, id)
    if pos != None:
        print("\tNómina del empleado: ", lstEmpl[pos][1])
        print("\tCódigo del empleado: ", lstEmpl[pos][0])
        print("\tHoras de trabajo: ", lstEmpl[pos][2])
        print("\tValor hora de trabajo: ", lstEmpl[pos][3])
        hora = lstEmpl[pos][2]
        valorhora =lstEmpl[pos][3]
        nomina=int(hora*valorhora)
        desEPS = 0.4*nomina
        desPEN = 0.4*nomina
        auxilioTrans = 140606
        salMin= 1160000
        print("-"*20)
        if nomina <= salMin:
            print(f"\t\tSalario: $ {nomina:,.0f} \n\
        \tDescuento EPS: $ {desEPS:,.0f}\n\
        \tDescuento Pensión: $ {desPEN:,.0f}\n\
        \tRequiere auxilio: Si\n\
        \tTotal: $ {nomina+desEPS+desPEN+auxilioTrans:,.0f}")
        else:
            print(f"\t\tSalario: $ {nomina:,.0f} \n\
        \tDescuento EPS: $ {desEPS:,.0f}\n\
        \tDescuento Pensión: $ {desPEN:,.0f}\n\
        \tRequiere auxilio: No\n\
        \tTotal: $ {nomina+desEPS+desPEN:,.0f}")
    else:
        print("\nEl código no existe.")
def leerValHora(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 1:
                msgError("Error. Valor de las horas mayor que 0")
                continue
            return n
        except ValueError:
            msgError("Error. Valor de las Horas inválidas")
            continue

def leerHoras(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 1:
                msgError("Error. Horas mayor que 0")
                continue
            return n
        except ValueError:
            msgError("Error. Horas inválidas")
            continue
        
def leerNom(msg):
    while True:
        try:
            n = input(msg)
            if n == None or n.strip() == "":
                print("Error Nombre inválido.")
                continue
            return n
        except Exception as e:
            print("Ha sucedido un Error: ", e)
            continue
        
def leerNumero(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 1:
                msgError("Error. Número mayor que 0")
                continue
            return n
        except ValueError:
            msgError("Error. Número inválido")
            continue

def agregarEmpleado(lstEmpl):
    print("\n\n*** 1. Agregar empleado - ACME ***\n")
    
    id = leerId("Id del empleado: ")
    nom = leerNom("Nombre del empleado: ")
    hora = leerHoras("Horas trabajadas: ")
    valh = leerValHora("Valor de la Hora trabajada: ")
    
    datempl = [id, nom, hora, valh]
    lstEmpl.append(datempl) 
    # print(lstEmpl)
    # input()

def menu():
    while True:
        try:
            print("\n\n*** NOMINA ACME ***")
            print("\tMENU")
            print("1- Agregar empleado\n\
2- Modificar empleado\n\
3- Buscar empleado\n\
4- Eliminar empleado\n\
5- Listar empleados\n\
6- Listar nómina de un empleado\n\
7- Listar nómina de todos los empleados\n\
8- Salir\n")
            op = int(input("\t>> Escoja una opción (1-8)?: "))
            if op < 1 or op > 8:
                msgError("Error. Opción Inválida (de 1 a 8).")
                continue
            return op
        except ValueError:
            msgError("Error. Opción Inválida (de 1 a 8).")
            continue
        
def main():
    lstEmpl = [[1, "Mauricio", 5, 1000],[2, "Angie", 40, 80000],[3, "Paola", 5, 3000]]
    while True:
        op = menu()
        if op == 1:
            agregarEmpleado(lstEmpl)
        elif op == 2:
            modificarEmpleado(lstEmpl)
        elif op == 3:
            buscarEmpleado(lstEmpl)
        elif op == 4:
            eliminaEmpleado(lstEmpl)
        elif op == 5:
            listaEmpleado(lstEmpl)
        elif op == 6:
            listaNomina(lstEmpl)
        elif op == 7:
            listaEmpleado(lstEmpl)
        elif op == 8:
            print("¿Realmente desea salir de la aplicación? \n 1. Si \n 2. No o presione cualquier otra tecla para terminar")
            chao=int(input())
            if chao==1:
                print("\n", "Gracias por usar el programa... Adios...".center(80))
                break
            else:
                continue

# Programa Principal
main()