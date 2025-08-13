from libro import Libro
class Biblioteca:
    def __init__(self):
        self.libros = []
    
    def agregar_libro(self, libro):
        self.libros.append(libro)
    
    def eliminar_libro(self, titulo):
        self.libros = [libro for libro in self.libros if libro.titulo != titulo]

    def listar_libros(self):
        for libro in self.libros:
            print(libro)
    
    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro
        return None
    
    def prestar_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        if libro:
            libro.estado = "Prestado"
            return True
        return False
    
    def devolver_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        if libro:
            libro.estado = "Disponible"
            return True
        return False

    
