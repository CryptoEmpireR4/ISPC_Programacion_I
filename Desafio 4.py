#Desafio 4 Calcular tiempo recorrido en diferentes tramos
n=int(1)
ing_tramo=int(input("Ingresar duración en minutos del Tramo "+str(n)+": "))
sum_tramos=ing_tramo
while ing_tramo!=0:
    n+=1
    ing_tramo=int(input((str("Ingresar duración en minutos del Tramo "+str(n)+": "))))
    sum_tramos= sum_tramos+ing_tramo
if len(str((int(sum_tramos%60))))==1:
    print("Tiempo empleado en horas y minutos: "+str(sum_tramos//60)+str(":0")+str((int(sum_tramos%60))))
else:print("Tiempo empleado en horas y minutos: "+str(sum_tramos//60)+str(":")+str((int(sum_tramos%60))))
