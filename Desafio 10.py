alfil=input("Ingresar Posicion del Alfil (letra para Columna (de la A a la h) y numero para Fila(del 1 al 8)): ")
torre=input("Ingresar Posicion de La Torre (letra para Columna (de la A a la h) y numero para Fila(del 1 al 8)): ")
col_tablero={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"g":8}
col_tablero_list=["A","B","C","D","E","F","G","H"]
alfil_col=int(col_tablero[alfil[0]])
alfil_fila=int(alfil[1])
torre_col=int(col_tablero[torre[0]])
torre_fila=int(torre[1])
mov_alfil=[]
col_insert=alfil_col
fil_insert=alfil_fila

while (alfil_col%2==0 and alfil_fila%2!=0) or (alfil_col%2!=0 and alfil_fila%2==0):
    alfil=input("Vuelva a ingresar Posicion deL ALFIL valida (letra para Columna (de la A a la h) y numero para Fila(del 1 al 8)): ")
    alfil_col=int(col_tablero[alfil[0]])
    alfil_fila=int(alfil[1])
while (torre_col%2==0 and torre_fila%2!=0) or (torre_col%2!=0 and torre_fila%2==0):
    torre=input("Vuelva a ingresar Posicion de La Torre valida (letra para Columna (de la A a la h) y numero para Fila(del 1 al 8)): ")
    torre_col=int(col_tablero[torre[0]])
    torre_fila=int(torre[1])

while 9>col_insert>0 and 9>fil_insert>0: #Movimiento Diagonal Abajo Izquierda
    mov_alfil.append(str(col_insert)+str(fil_insert))
    col_insert-=1
    fil_insert-=1

col_insert=alfil_col
fil_insert=alfil_fila

while 0<col_insert<9 and 9>fil_insert>0: #Movimiento Diagonal Abajo Derecha
    mov_alfil.append(str(col_insert)+str(fil_insert))
    col_insert+=1
    fil_insert-=1

col_insert=alfil_col
fil_insert=alfil_fila

while 9>col_insert>0 and 0<fil_insert<9: #Movimiento Diagonal Arriba Izquierda
    mov_alfil.append(str(col_insert)+str(fil_insert))
    col_insert-=1
    fil_insert+=1
col_insert=alfil_col
fil_insert=alfil_fila
    
while 0<col_insert<9 and 0<fil_insert<9: #Movimiento Diagonal Arriba Derecha
    mov_alfil.append(str(col_insert)+str(fil_insert))
    col_insert+=1
    fil_insert+=1

if alfil[0]==torre[0] or alfil[1]==torre[1]:
    print("Torre captura Alfil")
elif mov_alfil.count(str(torre_col)+str(torre_fila))>0:
    print("Alfil captura a Torre")
else:print("Ninguna Captura")
