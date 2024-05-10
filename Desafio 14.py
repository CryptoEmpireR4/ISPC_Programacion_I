signos = {
'aries': (( 3, 21), ( 4, 20)),
'tauro': (( 4, 21), ( 5, 21)),
'geminis': (( 5, 22), ( 6, 21)),
'cancer': (( 6, 22), ( 7, 23)),
'leo': (( 7, 24), ( 8, 23)),
'virgo': (( 8, 24), ( 9, 23)),
'libra': (( 9, 24), (10, 23)),
'escorpio': ((10, 24), (11, 22)),
'sagitario': ((11, 23), (12, 21)),
'capricornio': ((12, 22), ( 1, 20)),
'acuario': (( 1, 21), ( 2, 19)),
'piscis': (( 2, 20), ( 3, 20))}

validar_fecha=0

while validar_fecha!="si":
    año=input("Ingrese el año de su nacimiento: ")
    mes=int(input("Ingrese el mes de su nacimiento: "))
    dia=int(input("Ingrese el dia de su nacimiento: "))
    if mes==1 and 1<=dia<=31:
       validar_fecha="si"
    elif mes==2 and 1<=dia<=29:
        validar_fecha="si"
    elif mes==3 and 1<=dia<=31:
        validar_fecha="si"
    elif mes==4 and 1<=dia<=30:
        validar_fecha="si"
    elif mes==5 and 1<=dia<=31:
        validar_fecha="si"
    elif mes==6 and 1<=dia<=30:
        validar_fecha="si"
    elif mes==7 and 1<=dia<=31:
        validar_fecha="si"
    elif mes==8 and 1<=dia<=31:
        validar_fecha="si"
    elif mes==9 and 1<=dia<=30:
        validar_fecha="si"
    elif mes==10 and 1<=dia<=31:
        validar_fecha="si"
    elif mes==11 and 1<=dia<=30:
        validar_fecha="si"
    elif mes==12 and 1<=dia<=31:
        validar_fecha="si"
    else:"no"

fecha=(año,mes,dia)
año_dia=int(str(mes)+str(dia))
valida=0

mes*=100
print(fecha)
año_dia=int(mes+dia)

def determinar_signo(fecha):
    if 121>año_dia or 1221<año_dia<1231:
        print("capricornio")
    elif año_dia<=219:
        print("acuario")
    elif año_dia<=320:
        print("piscis")
    elif año_dia<=420:
        print("aries")
    elif año_dia<=521:
        print("tauro")
    elif año_dia<=621:
        print("geminis")
    elif año_dia<=723:
        print("cancer")
    elif año_dia<=823:
        print("leo")
    elif año_dia<=923:
        print("virgo")
    elif año_dia<=1023:
        print("libra")
    elif año_dia<=1122:
        print("escorpio")
    else:print("La fecha no corresponde a una fecha valida")
    valida="no"

determinar_signo(fecha)