#Desafio 5 Año Bisiesto
año=int(input("Ingrese el año que desea consultar: "))

if año > 1582:
    if año % 4 == 0 and año%400 !=0:
        print("Es bisiesto")
    else: print("No es bisiesto")
else:
    if año % 4 == 0:
        print("Es bisiesto")
    else: print("No es bisiesto")