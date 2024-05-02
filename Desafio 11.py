#Desafio 11 piedra, papel y tijera
#a=input("A: elija piedra, papel o tijera: ")
#b=input("B: elija piedra, papel o tijera: ")
a_triunfos=0
b_triunfos=0

#datos:
#tijera mata papel
#papel mata piedra
#piedra mata tijera

while int(a_triunfos)<3 or int(b_triunfos)<3:
    a=input("A: elija piedra, papel o tijera: ")
    b=input("B: elija piedra, papel o tijera: ")
    if a=="tijera" and b=="piedra":
        b_triunfos+=1
    elif a=="tijera" and b=="papel":
        a_triunfos+=1
    elif a=="papel" and b=="piedra":
        a_triunfos+=1
    elif a=="papel" and b=="tijera":
        b_triunfos+=1
    elif a=="piedra" and b=="papel":
        b_triunfos+=1
    elif a=="piedra" and b=="tijera":
        a_triunfos+=1
    if a_triunfos==3: break
    if b_triunfos==3: break
if a_triunfos==3:
    print("La persona A ha ganado por "+str(a_triunfos)+" a "+str(b_triunfos))
else:
    print("La persona B ha ganado por "+str(b_triunfos)+" a "+str(a_triunfos))