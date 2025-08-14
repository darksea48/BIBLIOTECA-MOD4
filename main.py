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
                nuevo_libro = Libro(id, titulo.strip(), autor.strip(), anio_publicacion)
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
                limpiar_pantalla()
                print("".center(50, '-'))
                print("Buscar libro".center(50, ' '))
                print("".center(50, '-'))
                libro_buscado = input("Ingrese el libro que deseas buscar (Puede ser el título o el autor): ")
                libro_seleccionado = biblioteca.buscar_libro(libro_buscado)
                if libro_seleccionado:
                    print(f"Libro encontrado:\nLibro: {libro_seleccionado.titulo}\nAutor: {libro_seleccionado.autor}\nAño de publicación: {libro_seleccionado.anio_publicacion}")
                    print("".center(50, '-'))
                    while True:
                        try:
                            print("Opciones:")
                            print("1. Marcar como prestado")
                            print("2. Devolver libro")
                            print("3. Editar datos del libro")
                            print("4. Eliminar libro")
                            print("9. Volver al menú principal")
                            subopcion = int(input("Elige una opción: "))
                        except ValueError:
                            print("Opción inválida. Intenta de nuevo.")
                            input("Presiona Enter para continuar...")
                        except Exception as e:
                            print(f"Ocurrió un error: {e}")
                            input("Presiona Enter para continuar...")
                        if subopcion == 1:
                            # Marcar como prestado
                            biblioteca.marcar_libro_prestado(libro_seleccionado, "Prestado")
                            input("Presiona Enter para continuar...")
                        elif subopcion == 2:
                            # Devolver libro
                            biblioteca.devolver_libro(libro_seleccionado, "Disponible")
                            input("Presiona Enter para continuar...")
                        elif subopcion == 3:
                            # Editar datos del libro
                            pregunta_titulo = input("¿Desea editar el título? (S/N) ").upper() == "S"
                            if pregunta_titulo == "S":
                                nuevo_titulo = input("Nuevo título: ")
                            pregunta_autor = input("¿Desea editar el autor? (S/N) ").upper() == "S"
                            if pregunta_autor == "S":
                                nuevo_autor = input("Nuevo autor: ")
                            pregunta_anio_publicacion = input("¿Desea editar el año de publicación? (S/N) ").upper() == "S"
                            if pregunta_anio_publicacion == "S":
                                nuevo_anio_publicacion = int(input("Nuevo año de publicación: "))
                            biblioteca.editar_libro(libro_seleccionado, nuevo_titulo, nuevo_autor, nuevo_anio_publicacion)
                            input("Presiona Enter para continuar...")
                        elif subopcion == 4:
                            # Eliminar libro
                            libro_eliminar = libro_seleccionado.id
                            rusur = input("¿Está seguro de que desea eliminar este libro? (S/N) ").upper()
                            if rusur == "S":
                                biblioteca.eliminar_libro(libro_seleccionado.id)
                                print("\nLibro eliminado.")
                                input("Presiona Enter para continuar...")
                                break
                            elif rusur == "N":
                                print("Eliminación de libro cancelada por el usuario.")
                            else:
                                print("Opción inválida. Intenta de nuevo.")
                            input("Presiona Enter para continuar...")
                        elif subopcion == 9:
                            break
                        else:
                            print("Opción inválida. Intenta de nuevo.")
                            input("Presiona Enter para continuar...")
                else:
                    print("Libro no encontrado.")
                    input("Presiona Enter para continuar...")
            elif opcion == 4:
                # Marcar libro como prestado
                try:
                    limpiar_pantalla()
                    print("Buscar libro a prestar".center(50, ' '))
                    libro_buscado = input("Ingrese el libro que deseas buscar (Puede ser el título o el autor): ")
                    libro_encontrado = biblioteca.buscar_libro(libro_buscado)
                    if libro_encontrado:
                        if libro_encontrado.get_estado() == "Prestado":
                            raise EstadoIdentico
                        else:
                            print("Libro encontrado:")
                            print(f"Título: {libro_encontrado.titulo}\nAutor: {libro_encontrado.autor}\nAño de publicación: {libro_encontrado.anio_publicacion}")
                            print("¿Desea marcar este libro como prestado? (S/N)")
                            respuesta = input().upper()
                            if respuesta == "S":
                                biblioteca.modificar_estado(libro_encontrado, "Prestado")
                                print("Libro marcado como prestado.")
                            else:
                                print("Operación cancelada.")
                    else:
                        raise LibroNoExiste
                except LibroNoExiste:
                    print("No se encontró el libro buscado.")
                except EstadoIdentico:
                    print("Este libro ya se encontraba prestado.")
                except Exception as e:
                    print(f"Ocurrió un error: {e}")
                input("Presiona Enter para continuar...")
            elif opcion == 5:
                # Marcar libro como devuelto
                try:
                    limpiar_pantalla()
                    print("Buscar libro a prestar".center(50, ' '))
                    libro_buscado = input("Ingrese el libro que deseas buscar (Puede ser el título o el autor): ")
                    libro_encontrado = biblioteca.buscar_libro(libro_buscado)
                    if libro_encontrado:
                        if libro_encontrado.get_estado() == "Prestado":
                            raise EstadoIdentico
                        else:
                            print("Libro encontrado:")
                            print(f"Título: {libro_encontrado.titulo}\nAutor: {libro_encontrado.autor}\nAño de publicación: {libro_encontrado.anio_publicacion}")
                            print(f"Título: {libro_encontrado.titulo}\nAutor: {libro_encontrado.autor}\nAño de publicación: {libro_encontrado.anio_publicacion}")
                            print("¿Desea marcar este libro como disponible nuevamente? (S/N)")
                            respuesta = input().upper()
                            if respuesta == "S":
                                biblioteca.modificar_estado(libro_encontrado, "Disponible")
                                print("Libro marcado como prestado.")
                            else:
                                print("Operación cancelada.")
                    else:
                        raise LibroNoExiste
                except LibroNoExiste:
                    print("No se encontró el libro buscado.")
                except EstadoIdentico:
                    print("Este libro ya se encontraba disponible.")
                except Exception as e:
                    print(f"Ocurrió un error: {e}")
                input("Presiona Enter para continuar...")
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