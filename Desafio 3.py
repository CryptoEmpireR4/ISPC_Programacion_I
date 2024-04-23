#Desafio 3 Determinar si un numero es primo o no
num= int(input("Inserte un numero: "))
resultados=[]

def lista_primo(num):
    for n in range(2, num):
        if num % n == 0:
          resultados.insert(1,"No")
lista_primo(num)

if int(len(resultados)) == 0:
    print("Es primo")
else: print("No es primo")