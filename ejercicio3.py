class Nota:
    def __init__(self, nota, nombre_Est):
        self.nota = nota
        self.nombre_Est = nombre_Est

    def ha_pasado(self):
        if self.nota >= 75:
            print(f"El/La estudiante {self.nombre_Est} ha aprobado.")
        else:
            print(f"El/La estudiante {self.nombre_Est} ha reprobado.")



nota_1 = Nota(80, "Julien")
nota_1.ha_pasado()
nota_2 = Nota(35, "Amélie")
print("La nota obtenida por Amélie en la primera corrección es:", nota_2.nota)
nota_2.nota = 70
print("Después de una segunda corrección, la nota de Amélie es:", nota_2.nota)
nota_2.ha_pasado()