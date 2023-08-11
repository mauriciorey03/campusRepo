# asignaturas={}
# CantMaterias=int(input("Ingrese la cantidad de materias: "))
# for i in range(1,CantMaterias+1):
#     materia=str(input("Ingrese el nombre de la materia: "))
#     notas=int(input("Ingrese la nota de cada asignatura: "))
#     asignaturas[materia]=notas

# for key, value  in asignaturas.items():
#     print(f"La nota en la {key} es : {value}")      

asignaturas={'Matemáticas':0,'Física':0,'Química':0,'Historia':0,'Lengua':0}

for materia in asignaturas:
    asignaturas= int(input("Ingrese nota: "))

for i, k in asignaturas.items():
    print(f"En {i} el estudiandte sacó {k}")