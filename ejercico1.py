import math

class FiguraGeometrica:
    def __init__(self, nombre):
        self.nombre = nombre

    def calcularArea(self):
        return 0

class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        FiguraGeometrica.__init__(self, "Círculo")
        self.radio = radio

    def calcular_Area(self):
        return math.pi * self.radio * self.radio

class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        FiguraGeometrica.__init__(self, "Rectángulo")
        self.base = base
        self.altura = altura

    def calcular_Area(self):
        return self.base * self.altura

class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        FiguraGeometrica.__init__(self, "Triángulo")
        self.base = base
        self.altura = altura

    def calcular_Area(self):
        return ((self.base * self.altura) / 2)
    


c = Circulo(5)
r = Rectangulo(4, 6)
t = Triangulo(3, 7)

print("Área círculo:", c.calcular_Area())
print("Área rectángulo:", r.calcular_Area())
print("Área triángulo:", t.calcular_Area())
