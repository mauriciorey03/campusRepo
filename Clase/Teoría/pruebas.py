def evaluacion(a,b,c):
    val1=int(a*0.3)
    val2=int(b*0.3)
    val3=int(c*0.4)
    resultado=val1+val2+val3
    if resultado >= 3:
        evalua=str("Aprueba")
    elif resultado< 3:
        evalua=str("Reprueba")
    return evalua


