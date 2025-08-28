class Personaje:
    def __init__(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel

    def atacar(self):
        return f"{self.nombre} hace ataque básico."


class Pilar(Personaje):
    def atacar(self):
        return f"{self.nombre} golpea con catana (daño {10 + self.nivel})."

class Demonio(Personaje):
    def atacar(self):
        return f"{self.nombre} lanza su ataque demoniaco (daño {12 + self.nivel})."

class Pilar_2(Personaje):
    def atacar(self):
        return f"{self.nombre} hace respiracion del rayo (daño {9 + self.nivel})."

equipo = [
    Pilar("Inosuke", 3),
    Demonio("Muzan", 5),
    Pilar_2("Zenitzu", 4)
]

print("\nATAQUES DEL EQUIPO")
for p in equipo:
    print(p.atacar())
