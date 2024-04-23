#Desafio 1 dar vuelta un numero de tres digitos
numero=input("Inserte un número entero de tres digitos: ")
while int(len(numero))!=3 or not numero.isnumeric(): #Determina si no tiene 3 cifras y no es numerico
    print("vuelta a intentar ingresar un numero de 3 cifras")
    numero=input("Inserte un número entero de tres digitos: ")
if int(len(numero))==3:
    str(numero)
    print(int(numero[2]+numero[1]+numero[0]))
else: 
    while int(len(numero))!=3:
     print("vuelta a intentar ingresar un numero de 3 cifras")
     numero=input("Inserte un número entero de tres digitos: ")
