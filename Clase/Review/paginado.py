
# doc = { ced1: {
#             nombre:"",
#             categoria: 0,
#             horastrab: 0
#         },
#
#         ced2: {
#             nombre:"",
#             categoria: 0,
#             horastrab: 0
#         }
#        }

cant = int(input("Cantidad de docentes"))
doc = {}
dic_cat = {1: 25000, 2: 30000, 3: 40000, 4: 45000, 5: 60000}
valTotal = 0
for i in range(1, cant+1):
    print("\nDatos del docente #", i)
    ced = int(input("Cedula? "))
    nom = input("Nombre? ")
    cat = int(input("Categoria (1 a 5)? "))
    ht = int(input("Horas trabajadas? "))

    valhono = dic_cat[cat] * ht
    datos = {
        "nombre": nom,
        "categoria": cat,
        "horas trab": ht,
        "honorarios": valhono
    }
    doc[ced] = datos

    valTotal += valhono

print("\n", "=" * 40)
print("** INFORME **")
print("=" * 40)
for k, v in doc.items():
    print(v["nombre"], "\t", f"${v['honorarios']:,.0f}")

print("\n", "=" * 40)
print("** RESUMEN **")
print("=" * 40)
print(f"Valor total de honorarios ${valTotal:,.0f}")
