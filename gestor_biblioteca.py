from biblioteca import Biblioteca
from libro import Libro
from libro_digital import LibroDigital

def mostrar_menu():
    print("\n--- Gestor de Biblioteca ---")
    print("1. Agregar libro")
    print("2. Eliminar libro")
    print("3. Ver todos los libros")
    print("4. Buscar libro")
    print("5. Marcar libro como prestado")
    print("6. Devolver libro")
    print("7. Salir")

def main():
    biblioteca = Biblioteca()

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == '1':
            tipo = input("¿El libro es digital? (s/n): ").strip().lower()
            titulo = input("Título: ")
            autor = input("Autor: ")
            anio = input("Año de publicación: ")

            if tipo == 's':
                formato = input("Formato (PDF, ePub, etc.): ")
                libro = LibroDigital(titulo, autor, anio, formato)
            else:
                libro = Libro(titulo, autor, anio)

            biblioteca.agregar_libro(libro)
            print(f"Libro '{titulo}' agregado.")

        elif opcion == '2':
            titulo = input("Título del libro a eliminar: ")
            try:
                biblioteca.eliminar_libro(titulo)
                print(f"Libro '{titulo}' eliminado.")
            except ValueError as e:
                print(f"Opción no válida: {e}")

        elif opcion == '3':
            print("\nLibros en la biblioteca:")
            biblioteca.listar_libros()

        elif opcion == '4':
            titulo = input("Título del libro a buscar: ")
            libro = biblioteca.buscar_libro(titulo)
            if libro:
                print(f"Resultado: {libro}")
            else:
                print("Libro no encontrado.")

        elif opcion == '5':
            titulo = input("Título del libro a prestar: ")
            try:
                if biblioteca.prestar_libro(titulo):
                    print(f"Libro '{titulo}' prestado.")
            except ValueError as e:
                print(f"Opción no válida: {e}")

        elif opcion == '6':
            titulo = input("Título del libro a devolver: ")
            try:
                if biblioteca.devolver_libro(titulo):
                    print(f"Libro '{titulo}' devuelto.")
            except ValueError as e:
                print(f"Opción no válida: {e}")

        elif opcion == '7':
            biblioteca.guardar_biblioteca()
            print("Biblioteca guardada. ¡Hasta pronto!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()

