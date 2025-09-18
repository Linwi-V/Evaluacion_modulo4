class Libro:
    def __init__(self, titulo, autor, anio_publicacion, estado="Disponible"):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.estado = estado

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Año: {self.anio_publicacion}, Estado: {self.estado}"

    def get_titulo(self):
        return self.titulo

    def get_autor(self):
        return self.autor

    def get_anio_publicacion(self):
        return self.anio_publicacion

    def get_estado(self):
        return self.estado

    def set_estado(self, nuevo_estado):
        self.estado = nuevo_estado


