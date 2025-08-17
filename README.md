# Gestor de Biblioteca (CLI)

Este es un sistema de gestión de biblioteca basado en una interfaz de línea de comandos (CLI), desarrollado en Python. Permite a los usuarios realizar operaciones básicas de CRUD (Crear, Leer, Actualizar, Eliminar) sobre una colección de libros, tanto físicos como digitales.

## ✨ Características Principales

- **Agregar nuevos libros**: Permite añadir libros físicos y digitales al catálogo.
- **Ver catálogo completo**: Muestra una lista de todos los libros en la biblioteca con sus detalles.
- **Buscar un libro**: Busca libros por su título o por su ID único.
- **Modificar estado**: Cambia el estado de un libro entre "Disponible" y "Prestado".
- **Editar información**: Actualiza los datos de un libro existente (título, autor, año).
- **Eliminar libros**: Borra libros del catálogo.
- **Gestión de ediciones digitales**: Permite crear y eliminar versiones digitales (PDF, EPUB) de un libro.
- **Persistencia de datos**: Guarda todos los cambios en un archivo de texto (`biblioteca.txt`) para que la información no se pierda al cerrar la aplicación (por el momento se guardará en un archivo .txt, luego se innovará a otro tipo de archivos, o a una base de datos).

## 📋 Requisitos

- Python 3.x

## 🚀 Instalación y Uso

No se requiere instalación de paquetes adicionales. Solo necesitas tener Python instalado en tu sistema.

1.  Clona o descarga este repositorio en tu máquina local.
2.  Navega al directorio del proyecto desde tu terminal:
    ```bash
    cd ruta/a/BIBLIOTECA-MOD4
    ```
3.  Para iniciar la aplicación, ejecuta el script `main.py`:
    ```bash
    python main.py
    ```

Una vez iniciado, se presentará un menú con las diferentes opciones disponibles. Sigue las instrucciones en pantalla para gestionar la biblioteca.

## 📂 Estructura del Proyecto

```
BIBLIOTECA-MOD4/
├── Clases.py           # Define las clases principales (Libro, Biblioteca) y excepciones.
├── funciones.py        # Contiene funciones de utilidad (cargar/guardar datos, limpiar pantalla).
├── main.py             # Punto de entrada de la aplicación, contiene el menú y la lógica de usuario.
├── biblioteca.txt          # Archivo de texto que actúa como base de datos.
└── README.md           # Este archivo.
```

### Descripción de Archivos Clave

- **`main.py`**: El punto de entrada de la aplicación. Contiene el bucle principal del menú y gestiona la interacción con el usuario, llamando a los métodos correspondientes de la clase `Biblioteca`.
- **`Clases.py`**: El corazón del modelo de datos.
    - `Libro`: Clase base para los libros físicos.
    - `LibroDigital`: Clase que hereda de `Libro` y añade funcionalidades para formatos digitales.
    - `Biblioteca`: Clase principal que orquesta todas las operaciones sobre la colección de libros.
    - `Excepciones personalizadas`: `LibroNoExiste`, `EstadoIdentico`, `FormatoNoExistente` para un manejo de errores más específico.
- **`funciones.py`**: Módulo con funciones de apoyo, como `cargar_datos` y `guardar_datos`, para abstraer la lógica de lectura y escritura del archivo de persistencia.

## ✒️ Autor

- **Douglas Suárez Z**