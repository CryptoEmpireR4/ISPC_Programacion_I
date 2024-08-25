
#Conversor de Monedas 1.0:
tc={"USD":float(1.0),"ARS":float(0.0011),"BRL":float(0.180),"CLP":float(0.0011)}#Diccionario de Tipos de Cambio con USD moneda de base
class Moneda():
    def __init__(self,moneda,cantidad,tc):
        self.moneda=moneda
        self.cantidad=cantidad
        self.tc=tc
    def cambiar_moneda(self,cantidad):
        self.cantidad=cantidad*self.tc
    def __str__(self):
        return self.cantidad
print("Bienvenido a nuestro conversor de Monedas 1.0")
print("Codigos de Monedas Disponbles:")
print("USD = DOLAR NORTEAMERICANO")
print("ARS = PESO ARGENTINO")
print("BRL = REAL BRASILEÑO")
print("CLP = PESO CHILENO")
cantidad=int(input("Ingrese la cantidad a convertir: "))#ingresa la cantidad a convertir
moneda=input("Ingrese el codigo de la moneda a convertir: ")#ingresa la cantidad a convertir
traspaso=input("¿A que moneda desea convertir? (Ingrese el codigo de la moneda): ")#Ingresa la moneda a la cual deseamos convertir nuestra tenencia
tc=tc[moneda]/tc[traspaso]
cambio=Moneda(moneda,cantidad,tc)
cambio.cambiar_moneda(cantidad)
print("Su tenencia se convertira en: "+str(round(cambio.cantidad,2))+" "+traspaso)