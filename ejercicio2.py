class Personaje:
    def __init__(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel

    def atacar(self):
        print(self.nombre, "ataca con fuerza.")

class Jugador(Personaje):
    def __init__(self, nombre, nivel, clase):
        Personaje.__init__(self, nombre, nivel)
        self.clase = clase

    def usarHabilidadEspecial(self):
        print(self.nombre, "usa su habilidad especial de", self.clase)

class Enemigo(Personaje):
    def __init__(self, nombre, nivel, tipo):
        Personaje.__init__(self, nombre, nivel)
        self.tipo = tipo

    def gritar(self):
        print(self.nombre, "el", self.tipo, "del fuego", "Hace la novena postura")


jug = Jugador("Gyutaru", 10, "Demonio")
ene = Enemigo("Rengoku", 8, "Pilar")

jug.atacar()
jug.usarHabilidadEspecial()
ene.atacar()
ene.gritar()
