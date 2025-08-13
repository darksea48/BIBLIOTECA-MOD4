from funciones import *

class LibroNoExiste(Exception):
    pass

class EstadoIdentico(Exception):
    pass

class Libro:
    def __init__(self, id, titulo, autor, anio_publicacion, estado="Disponible"):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.__estado = estado
    
    def get_estado(self):
        return self.__estado
    
    def set_estado(self, estado):
        self.__estado = estado
    
    def __str__(self):
        return f"{self.id},{self.titulo},{self.autor},{self.anio_publicacion},{self.__estado}"

class LibroDigital(Libro):
    def __init__(self, id, titulo, autor, anio_publicacion, estado, formato):
        super().__init__(id, titulo, autor, anio_publicacion, estado)
        self.formato = formato
    
    def __str__(self):
        return super().__str__() + f", Formato: {self.formato}"

class Biblioteca:
    try:
        with open(ARCHIVO, 'r', encoding='utf-8'):
            pass
    except FileNotFoundError:
        with open(ARCHIVO, 'w', encoding='utf-8'):
            pass
    
    def __init__(self):
        self.libros = []
        datos = cargar_datos(ARCHIVO)
        if datos:
            for libro_str in datos:
                id, titulo, autor, anio_publicacion, estado = libro_str.split(',')
                libro = Libro(id, titulo, autor, anio_publicacion, estado)
                self.libros.append(libro)
    
    def agregar_libro(self, libro):
        self.libros.append(libro)
        agregar_dato(ARCHIVO, libro)
        print(f"Se agregó el libro: {libro.titulo}")
    
    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro
        return None
    
    def eliminar_libro(self, titulo):
        try:
            for libro in self.libros:
                if libro.titulo == titulo:
                    self.libros.remove(libro)
                    print(f"Se eliminó el libro: {libro.titulo}")
                    return
            raise LibroNoExiste
        except LibroNoExiste:
            print(f"No se encontró el libro con el título: {titulo}")
    
    def mostrar_libros(self):
        if not self.libros:
            print("No hay libros en la biblioteca.")
        else:
            print("Libros en la biblioteca:")
            for libro in self.libros:
                print("".center(50, '-'))
                print(f"ID Libro: {libro.id}\nTítulo: {libro.titulo}\nAutor: {libro.autor}\nAño de Publicación: {libro.anio_publicacion}\nEstado: {libro.get_estado()}")
                print("".center(50, '-'))
    
    def modificar_estado(self, titulo, nuevo_estado):
        try:
            libro = self.buscar_libro(titulo)
            if libro:
                if libro.get_estado() == nuevo_estado:
                    raise EstadoIdentico
                Libro.set_estado(libro, nuevo_estado)
                print(f"Se modificó el estado del libro: {libro.titulo}. Pasó a estar {nuevo_estado}.")
            else:
                raise LibroNoExiste
        except LibroNoExiste:
            print(f"No se encontró el libro con el título: {titulo}")
        except EstadoIdentico:
            print(f"Este libro ya se encontraba {nuevo_estado}")
    

    def editar_datos(self, titulo, nuevo_titulo, nuevo_autor, nuevo_anio_publicacion):
        libro = self.buscar_libro(titulo)
        if libro:
            libro.titulo = nuevo_titulo
            libro.autor = nuevo_autor
            libro.anio_publicacion = nuevo_anio_publicacion
    
    def cerrar_biblioteca(self):
        guardar_datos(ARCHIVO, self.libros)