class Paleta:
    def __init__(self, sabor):
        self.sabor = sabor

    def precio(self):
        return 0.0

    def descripcion(self):
        return f"Paleta genérica de {self.sabor}"

class PaletaAgua(Paleta):
    def precio(self):
        return 15.0

    def descripcion(self):
        return f"Paleta de agua sabor {self.sabor}"

class PaletaLeche(Paleta):
    def precio(self):
        return 20.0

    def descripcion(self):
        return f"Paleta de leche sabor {self.sabor}"

class PaletaRellena(Paleta):
    def __init__(self, sabor, relleno):
        super().__init__(sabor)
        self.relleno = relleno

    def precio(self):
        return 25.0

    def descripcion(self):
        return f"Paleta rellena de {self.sabor} con {self.relleno}"

pedido = [
    PaletaAgua("frsa"),
    PaletaLeche("platano"),
    PaletaRellena("Chocolate", "galletas")
]

total = 0
for p in pedido:
    print(f"- {p.descripcion()} -> ${p.precio():.2f}")
    total += p.precio()
print(f"Total a pagar: ${total:.2f}")
