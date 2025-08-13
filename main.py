from libro import Libro
from biblioteca import Biblioteca

def main():
    biblioteca = Biblioteca()
    
    while True:
        print("\n--- Menú de Biblioteca ---")
        print("1. Agregar libro")
        print("2. Eliminar libro")
        print("3. Listar libros")
        print("4. Buscar libro")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            anio_publicacion = input("Ingrese el año de publicación: ")
            estado = "Disponible"
            nuevo_libro = Libro(titulo, autor, anio_publicacion, estado)
            biblioteca.agregar_libro(nuevo_libro)
            print(f"Libro '{titulo}' agregado exitosamente.")
        
        elif opcion == '2':
            titulo = input("Ingrese el título del libro a eliminar: ")
            biblioteca.eliminar_libro(titulo)
            print(f"Libro '{titulo}' eliminado exitosamente.")
        
        elif opcion == '3':
            print("\nLista de libros:")
            biblioteca.listar_libros()
        
        elif opcion == '4':
            titulo = input("Ingrese el título del libro a buscar: ")
            libro = biblioteca.buscar_libro(titulo)
            if libro:
                print(libro)
            else:
                print(f"Libro '{titulo}' no encontrado.")
        
        elif opcion == '5':
            titulo = input("Ingrese el título del libro a prestar: ")
            if biblioteca.prestar_libro(titulo):
                print(f"Libro '{titulo}' prestado exitosamente.")
            else:
                print(f"Libro '{titulo}' no disponible para préstamo.")
        
        elif opcion == '6':
            titulo = input("Ingrese el título del libro a devolver: ")
            if biblioteca.devolver_libro(titulo):
                print(f"Libro '{titulo}' devuelto exitosamente.")
            else:
                print(f"Libro '{titulo}' no encontrado o ya está disponible.")
        
        elif opcion == '7':
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()
