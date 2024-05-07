jug1=input("Nombra al 1er preclasificado al torneo: ")
jug2=input("Nombra al 2do preclasificado al torneo: ")
jug3=input("Nombra al 3er preclasificado al torneo: ")
jug4=input("Nombra al 4to preclasificado al torneo: ")
jug5=input("Nombra al 5to preclasificado al torneo: ")
jug6=input("Nombra al 6to preclasificado al torneo: ")
jug7=input("Nombra al 7mo preclasificado al torneo: ")
jug8=input("Nombra al 8vo preclasificado al torneo: ")

print("Ronda 1")
print("Elegir ganador usando la a o la b")
cuartos1=input("a- "+jug1+"vs b- "+jug8+": ")
cuartos2=input("a- "+jug2+"vs b- "+jug7+": ")
cuartos3=input("a- "+jug3+"vs b- "+jug6+": ")
cuartos4=input("a- "+jug4+"vs b- "+jug5+": ")

if cuartos1 == "b":
    jug1=jug8
else: jug1=jug1

if cuartos2 == "b":
    jug2=jug7
else: jug2=jug2

if cuartos3 == "b":
    jug3=jug6
else: jug3=jug3

if cuartos3 == "b":
    jug4=jug5
else: jug4=jug4

print("Ronda 2")
print("Elegir ganador usando la a o la b")
semis1=input("a- "+jug1+"vs b- "+jug4+": ")
semis2=input("a- "+jug2+"vs b- "+jug3+": ")

if semis1 == "b":
    jug1=jug4
else: jug1=jug1

if semis2 == "b":
    jug2=jug3
else: jug2=jug2

print("Final")
print("Elegir ganador usando la a o la b")
final1=input("a- "+jug1+"vs b- "+jug2+": ")

if semis2 == "b":
    print("Campeon "+jug2)
else: print("Campeon "+jug1)