#Algortimo para calcular el salario esmanal de un trabajdor 
#dados su tarifa horaria y horas diarias trabajadas
'''
variables:
    relaes: tarifa, horas diarias, salario
'''

#Asumo que trabaja los 7 dias de la semana xd
def salario_semanal(tarifa_horaria,horas_diarias):
    return horas_diarias * tarifa_horaria * 7

horas_diarias = int(input("Digamos las horas que trabaja al dia: "))
tarifa_horaria = float(input("¿Cuanto le pagan por una hora de trabajo?: "))
print(f"El salario semanal que usted gana es de: {salario_semanal(horas_diarias, tarifa_horaria)}")