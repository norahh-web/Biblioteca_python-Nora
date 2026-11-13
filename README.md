# Sistema de gestión de biblioteca

Proyecto final de Python con programación orientada a objetos. Es un programa de consola para gestionar los libros y los socios de una biblioteca: préstamos, devoluciones, búsquedas y altas. Los datos se leen y se guardan en ficheros de texto.

## Cómo ejecutarlo

1. Tener Python 3 instalado.
2. Clonar el repositorio.
3. Desde la carpeta raíz del proyecto, ejecutar:

```
python main.py
```

## Estructura del proyecto

```
controlador/
    biblioteca.py       lógica de la biblioteca (préstamos, devoluciones, búsquedas, altas)
    almacenamiento.py   cargar y guardar los ficheros y escribir el log
datos/
    libros.txt          100 libros
    socios.txt          15 socios
    log.txt             registro de eventos (se crea solo)
errores/
    libro_no_disponible.py   excepción personalizada
modelo/
    Libro.py
    Socio.py
vista/
    menu.py             menú por consola
main.py
```

## Menú

1. Mostrar todos los libros
2. Mostrar los libros disponibles
3. Buscar un libro por el título (sin importar mayúsculas o minúsculas)
4. Prestar un libro a un socio
5. Devolver el libro de un socio
6. Mostrar los socios que tienen un libro
7. Añadir libros o socios
8. Salir (se guardan los cambios en los ficheros)

## Ficheros de datos

Una línea por registro, con los campos separados por `;`. Si no hay préstamo, el último campo es `None`.

```
libros.txt: codigo;titulo;autor;anio;categoria;codigo_socio
socios.txt: codigo_socio;nombre;email;codigo_libro
```

## Log

Los préstamos, las devoluciones y las altas se guardan en `datos/log.txt` con este formato:

```
[fecha][evento][detalles]
```

## Mejoras posibles

- Poder borrar libros y socios.
- Permitir que un socio tenga más de un libro a la vez.
- Guardar fecha de préstamo y de devolución, y avisar de los retrasos.
- Buscar también por autor, categoría o año.
- Validar el formato del email al añadir un socio.
- Mejorar el formato de las listas (columnas alineadas).
- Guardar un historial de préstamos de cada libro y de cada socio.
- Usar una base de datos en lugar de ficheros de texto.
- Hacer una interfaz gráfica o una versión web.
