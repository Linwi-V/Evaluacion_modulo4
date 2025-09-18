import os
from libro import Libro
from libro_digital import LibroDigital

class Biblioteca:
    def __init__(self, archivo="biblioteca.txt"):
        self.archivo = archivo
        self.libros = []
        self.cargar_biblioteca()

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def eliminar_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        if libro:
            self.libros.remove(libro)
        else:
            raise ValueError(f"No se encontró el libro '{titulo}' para eliminar.")

    def listar_libros(self):
        if not self.libros:
            print("No hay libros en la biblioteca.")
        for libro in self.libros:
            print(libro)

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.get_titulo().lower() == titulo.lower():
                return libro
        return None

    def prestar_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        if libro:
            if libro.get_estado() == "Disponible":
                libro.set_estado("Prestado")
                return True
            else:
                raise ValueError(f"El libro '{titulo}' ya está prestado.")
        else:
            raise ValueError(f"No se encontró el libro '{titulo}'.")

    def devolver_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        if libro:
            if libro.get_estado() == "Prestado":
                libro.set_estado("Disponible")
                return True
            else:
                raise ValueError(f"El libro '{titulo}' ya está disponible.")
        else:
            raise ValueError(f"No se encontró el libro '{titulo}'.")

    def cargar_biblioteca(self):
        if not os.path.exists(self.archivo):
            return  # No hay archivo aún

        with open(self.archivo, "r", encoding="utf-8") as f:
            for linea in f:
                datos = linea.strip().split("||")
                if len(datos) >= 4:
                    tipo = datos[0]
                    titulo = datos[1]
                    autor = datos[2]
                    anio = datos[3]
                    estado = datos[4] if len(datos) > 4 else "Disponible"

                    if tipo == "LibroDigital":
                        formato = datos[5] if len(datos) > 5 else "PDF"
                        libro = LibroDigital(titulo, autor, anio, formato, estado)
                    else:
                        libro = Libro(titulo, autor, anio, estado)

                    self.agregar_libro(libro)

    def guardar_biblioteca(self):
        with open(self.archivo, "w", encoding="utf-8") as f:
            for libro in self.libros:
                if isinstance(libro, LibroDigital):
                    linea = f"LibroDigital||{libro.titulo}||{libro.autor}||{libro.anio_publicacion}||{libro.estado}||{libro.formato}"
                else:
                    linea = f"Libro||{libro.titulo}||{libro.autor}||{libro.anio_publicacion}||{libro.estado}"
                f.write(linea + "\n")
            print(f"Biblioteca guardada en '{self.archivo}'")

    
