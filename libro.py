class Libro:
    libros = []
    def __init__(self, titulo, autor, anio_publicacion, estado):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.estado = estado

    def __str__(self):
        return f"{self.titulo} por {self.autor} ({self.anio_publicacion}) - Estado: {self.estado}"
    
    def get_titulo(self):
        return self.titulo
    def get_autor(self):
        return self.autor
    def get_anio_publicacion(self):
        return self.anio_publicacion
    
    def set_estado(self):
        return self.estado

