#Desafio 7 secuencia de Collatz
num=int(input("Ingrese un número: "))
list_collatz=[num]
lista_edit=0
while num>1:
    if num%2==0:
        list_collatz.append(int(num/2))
        num=num/2
    else: 
        list_collatz.append(int(num*3+1))
        num=num*3+1
lista_edit=str(list_collatz)
lista_edit=str.replace(lista_edit,",","")
lista_edit=str.replace(lista_edit,"[","")
lista_edit=str.replace(lista_edit,"]","")
print(lista_edit)

