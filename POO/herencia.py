class Vehiculo:
    def __init__(self,color):
        self.color = color

    def get_ruedas(self):
        return self.ruedas 

    def get_color(self):
        return self.color

class Coche(Vehiculo):
    ruedas = 4

class Moto(Vehiculo):
    ruedas = 2

c = Coche("Rojo")
#c.set_color("Rojo")
color = c.get_color()
ruedas = c.get_ruedas()
print(ruedas)
print(color)