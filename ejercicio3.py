class Paleta:
    def __init__(self, sabor, precio):
        self.sabor = sabor
        self.precio = precio

    def mostrarInformacion(self):
        print("Sabor:", self.sabor, "Precio:", self.precio, "pesos")

class PaletaAgua(Paleta):
    def __init__(self, sabor, precio, baseAgua=True):
        Paleta.__init__(self, sabor, precio)
        self.baseAgua = baseAgua

        self.precio = self.precio + 2

    def mostrarBaseAgua(self):
        print("Base de agua:", self.baseAgua)

class PaletaCrema(Paleta):
    def __init__(self, sabor, precio, cremosa=True):
        Paleta.__init__(self, sabor, precio)
        self.cremosa = cremosa
        self.precio = self.precio + 6

    def mostrarTexturaCremosa(self):
        print("¿Cremosa?:", self.cremosa)


    def aplicarDescuento(self, descuento):
        self.precio = self.precio - descuento

    def cambiarSabor(self, nuevo_sabor):
        self.sabor = nuevo_sabor

p1 = PaletaAgua("menta", 10)
p2 = PaletaCrema("Napolitano", 12)

p1.mostrarInformacion()
p1.mostrarBaseAgua()

p2.mostrarInformacion()
p2.mostrarTexturaCremosa()
p2.aplicarDescuento(3)
p2.cambiarSabor("Mango con chile")
p2.mostrarInformacion()
