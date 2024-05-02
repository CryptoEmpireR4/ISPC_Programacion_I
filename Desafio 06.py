#Desafio 6 Triangulo
renglones= int(input("ingrese el numero de renglones: "))
fila=[]
filas=0
for n in range(1,renglones+1):
        fila.append(n*2)
        fila.sort(reverse=True)
        filas=str(fila)
        filas=str.replace(filas,",","")
        filas=str.replace(filas,"[","")
        filas=str.replace(filas,"]","")
        print (filas)
