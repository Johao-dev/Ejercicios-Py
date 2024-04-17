

#nota etnre = 20%
#nota exa = 80%

notaEntregable = int(input("ingrese nota entre: "))
notaExamen = int(input("Ingrese nota examne: "))

notaEntregable = notaEntregable * 0.20
notaExamen = notaExamen * 0.8

print("nota final: ", (notaExamen + notaEntregable))