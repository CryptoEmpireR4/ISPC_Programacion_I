paises = {
'Pepito': {'Chile', 'Argentina'},
'Yayita': {'Francia', 'Suiza', 'Chile'},
'John': {'Chile', 'Italia', 'Francia', 'Peru'},
}
elec1=input("Elegir entre Pepito, Yayita y John: ")
elec2=input("Elegir entre Pepito, Yayita y John: ")

while elec1==elec2:
 print("Has repetido la eleccion 1")
 elec2=input("Elegir entre Pepito, Yayita y John: ")

aparicion=0
largo=len(paises[elec2])-1
lista1=(list(paises[elec1]))
lista2=(list(paises[elec2]))

while largo > -1:
 aparicion+=lista1.count(lista2[largo])
 largo-=1

print("Existen "+str(aparicion)+" paises visitados en comun")
 
 