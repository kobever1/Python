class coche():

    def __init__(self,ruedas,color):
        self.color = color
        self.ruedas = ruedas

    def verColor(self):
        print(self.color)

    def arrancar(self):
        print("brum brum")

    

fiatpanda = coche(4, "Rojo")
fiatpanda.verColor()

"""print(fiatpanda.ruedas)
print(fiatpanda.color
"""