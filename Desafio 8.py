#Desafio 8 Campus Vitacura
eleccion=input("Ingrese el producto a eleccion: ")
precio=0
ingresado=0
diccionario_art={"A":270,"B":340,"C":390}
precio= diccionario_art[eleccion]
print("EL precio del producto es $ "+str(precio))

while ingresado <= int(precio):
    ingresado=ingresado
    ingreso=int(input("ingrese monedas: "))
    ingresado=ingresado+ingreso  

vuelto=ingresado-precio
print("El precio del Producto "+str(eleccion)+" es $ "+str(precio)+" y ha ingresado $ "+str(ingresado)+" en monedas. Su vuelto es de $ "+str(vuelto))
print("Entrego las siguientes monedas de vuelto:")
while vuelto>0:
    if vuelto>=100:
        vuelto-=100
        print(100)
    else: 
        if vuelto>=50:
            vuelto-=50
            print(50)
        else: 
            vuelto -=10
            print(10)
