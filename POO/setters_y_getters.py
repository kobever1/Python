from cgi import print_arguments

from secretstorage import get_collection_by_alias


class Coche:
    def __init__(self):
        pass
    def set_color(self,color):
        self.color = color
    def get_color(self):
        return self.color



c = Coche()
c.set_color("Azul")

color = c.get_color()

print(c.color)