#Desafio 2: Contar Horas
hora=int(input("Inserte cual es la hora actual: "))
contar=int(input("Inserte las horas a contar desde la hora actual: "))
horario=(hora+contar) % 24
print("Pasando "+str(contar)+" desde la hora actual, el reloj daria que son las "+str(horario)+" horas.")