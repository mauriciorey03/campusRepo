directorio={}
while True:
    try:
        print(directorio)
        add=int(input("Desea agregar 1. Si - 2.Parar"))
        if add== 2:
            break
        nom = input ("Ingrese el nombre: ")
        if nom in directorio:
            print("No puede incluir dos veces el mismo contacto.")
            continue
        num = int(input("Ingrese el teléfono: "))
        if nom not in directorio:
            directorio[nom]=num
            continue
    except ValueError:
        print("Intentelo de nuevo")