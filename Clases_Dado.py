import random

class Dado:
    def _init_(self,cara):
        self.cara=cara
    def tirar_dado(self,numero):
        self.cara=numero


tiro=Dado()
tiro.tirar_dado(random.randint(1, 6)) #uso la formula para definir un numero aleatorio
print(tiro.cara)





