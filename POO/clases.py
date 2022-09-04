class vehiculo:
    ruedas = 0
    color = None

    def arrancar(self):
        print("brum brum")

class coche(vehiculo):
    ruedas = 4

class moto(vehiculo):
    ruedas = 2

fiatpanda = coche()
fiatpanda.color = "Rojo"

mimoto = moto()
mimoto.color = "Verde"

print((fiatpanda.color))
print((fiatpanda.arrancar()))

print((mimoto.color))
print((mimoto.ruedas))

#print(type(fiatpanda))

