import math

class Circulo:
    
    def __init__(self, x, y, R):
        self.x = x
        self.y = y
        self.radio = R

   
    def area(self):
        return math.pi * (self.radio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.radio

    def mostrar_propiedades(self):
        return f"El círculo tiene un radio de {self.radio} cm, y su centro es O({self.x},{self.y})"


circulo_1 = Circulo(3, 4, 5)

print(circulo_1.mostrar_propiedades())

print("El perímetro del círculo 1 es:", round(circulo_1.perimetro(), 2))

print("El área del círculo 1 es:", round(circulo_1.area(), 2))