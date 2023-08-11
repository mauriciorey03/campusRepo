
# estudiantes = { cod1: {
#             nombre:"",
#             nota 1:"",
#             nota2:"",
#             nota3;"",
#             resultado: Aprueba/Reprueba
#         },
#               cod2: {
#             nombre:"",
#             nota 1:"",
#             nota2:"",
#             nota3;"",
#             resultado: Aprueba/Reprueba
#         },

def evaluacion(a,b,c):
    val1=int(a*0.3)
    val2=int(b*0.3)
    val3=int(c*0.4)
    resultado=val1+val2+val3
    if resultado >= 3:
        evalua="Aprueba"
    elif resultado< 3:
        evalua="Reprueba"
    return evalua, resultado

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

def msgError(msg):
    print(msg)
    input("Presione cualquier tecla para continuar ...")

cant = int(input("Cantidad de estudiantes"))
doc = {}

while True:
        print("\nDatos del estudiante #",)
        id =leerNumero( "Código del estudiante: ")
        if id == 999:
            break
        nom = leerNom("Nombre? ")
        Nota1 = leerNumero("Ingrese la primera nota: ")
        Nota2 = leerNumero("Ingrese la segunda nota: ")
        Nota3 = leerNumero("Ingrese la tercera nota: ")
        aprueba, definitiva = evaluacion(Nota1,Nota2,Nota3)
        Resultado=aprueba

        datos={
            "nombre": nom,
            "nota 1": Nota1,
            "nota 2": Nota2,
            "nota 3": Nota3,
            "Total": definitiva,
            "Condición": Resultado
        }
        doc[id] = datos

print()
for k, v in doc.items():
    print("El estudiante ", v["nombre"],  v['Condición'])

