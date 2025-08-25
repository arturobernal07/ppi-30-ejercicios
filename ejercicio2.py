class libro:
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    def mostrar_informaciones(self):
        print(f"El libro: '{self.titulo}', escrito por: '{self.autor}', se vende a {self.precio} euros.")


libro_1 = libro("Donde te has ido mujer", "P. Elegante", 16)