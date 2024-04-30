palabra1=input("Ingrese la palabra 1, para comparar si es un anagrama: ")
palabra2=input("Ingrese la palabra 1, para comparar si es un anagrama: ")
pal1_list=[]
pal2_list=[]
largo_pal1=len(palabra1)
largo_pal2=len(palabra2)

while int(largo_pal1)>=0:
    largo_pal1-=1
    agregar=palabra1[int(largo_pal1)]
    pal1_list.append(agregar)

pal1_list=pal1_list[1:]

while int(largo_pal2)>=0:
    largo_pal2-=1
    agregar=palabra2[int(largo_pal2)]
    pal2_list.append(agregar)

pal2_list=pal2_list[1:]

pal1_list.sort()
pal2_list.sort()

print(pal1_list)
print(pal2_list)

if pal1_list==pal2_list:
    print("Son palabras ANAGRAMAS")
else: print("No son ANAGRAMAS")
