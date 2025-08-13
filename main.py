from Clases import *
from funciones import *
from random import randint

def menu():
    biblioteca = Biblioteca()
    while True:
        try:
            limpiar_pantalla()
            print("--- Gestor de Biblioteca ---")
            print("1. Agregar libro")
            print("2. Ver todos los libros")
            print("3. Buscar libro")
            print("4. Marcar libro como prestado")
            print("5. Devolver libro")
            print("9. Salir")
            opcion = int(input("Elige una opción: "))
            if opcion == 1:
                # Agregar libro
                limpiar_pantalla()
                print("Agregar libro".center(50, '-'))
                titulo = input("Título: ")
                autor = input("Autor: ")
                while True:
                    try:
                        anio_publicacion = int(input("Año de publicación: "))
                        if anio_publicacion < -5001 or anio_publicacion > 2026:
                            raise ValueError
                        elif not anio_publicacion.is_integer():
                            raise ValueError
                        break
                    except ValueError:
                        print("Debes ingresar un año correcto. Intenta de nuevo.")
                    except Exception as e:
                        print(f"Ocurrió un error: {e}")
                id = randint(1000, 9999)
                nuevo_libro = Libro(id, titulo, autor, anio_publicacion)
                biblioteca.agregar_libro(nuevo_libro)
                input("Presiona Enter para continuar...")
            elif opcion == 2:
                # Ver todos los libros
                limpiar_pantalla()
                print("".center(50, '-'))
                print("Libros de la biblioteca".center(50, ' '))
                print("".center(50, '-'))
                biblioteca.mostrar_libros()
                input("Presiona Enter para continuar...")
            elif opcion == 3:
                pass
            elif opcion == 4:
                pass
            elif opcion == 5:
                pass
            elif opcion == 9:
                biblioteca.cerrar_biblioteca()
                break
            else:
                print("Opción inválida. Intenta de nuevo.")
        except ValueError:
            print("Opción inválida. Debes ingresar un número entero. Intenta de nuevo.")
            input("Presiona Enter para continuar...")
        except KeyboardInterrupt:
            print()
            print("Operación cancelada por el usuario. Se cierra el programa.")
            break
        except Exception as e:
            print(f"Ocurrió un error: {e}")
            input("Presiona Enter para continuar...")


menu()
print("Gracias por usar el gestor de biblioteca.")  