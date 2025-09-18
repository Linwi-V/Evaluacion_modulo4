from libro import Libro

class LibroDigital(Libro):
    def __init__(self, titulo, autor, anio_publicacion, formato, estado="Disponible"):
        super().__init__(titulo, autor, anio_publicacion, estado)
        self.formato = formato

    def __str__(self):
        return super().__str__() + f", Formato: {self.formato}"
