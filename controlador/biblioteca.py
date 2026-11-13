from modelo.Libro import Libro
from modelo.Socio import Socio

from errores.libro_no_disponible import LibroNoDisponibleError
from controlador.almacenamiento import cargar_libros, cargar_socios, guardar_libros, guardar_socios, registrar_log

class Biblioteca:
    def __init__(self):
        self.libros = cargar_libros()
        self.socios = cargar_socios()

    def buscar_libro(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro
        return None

    def buscar_socio(self, id_socio):
        for socio in self.socios:
            if socio.id_socio == id_socio:
                return socio
        return None

    def libros_disponibles(self):
        disponibles = []
        for libro in self.libros:
            if libro.esta_disponible():
                disponibles.append(libro)
        return disponibles
    
    def buscar_por_titulo(self, texto):
        encontrados = []
        for libro in self.libros:
            if texto.lower() in libro.titulo.lower():
                encontrados.append(libro)
        return encontrados

    def socios_con_libro(self):
        con_libro = []
        for socio in self.socios:
            if socio.tiene_libro():
                con_libro.append(socio)
        return con_libro

    def prestar_libro(self, isbn, id_socio):
        libro = self.buscar_libro(isbn)
        socio = self.buscar_socio(id_socio)

        #Para validar la existencia
        if libro is None:
            raise ValueError("no existe ese libro")
        if socio is None:
            raise ValueError("no existe ese socio")

        # validar disponibilidad/estado
        if not libro.esta_disponible():
            raise LibroNoDisponibleError("el libro lo tiene otro socio", isbn)
        if socio.tiene_libro():
            raise ValueError("el socio ya tiene un libro")

        libro.id_socio = id_socio
        socio.isbn_prestado = isbn
        registrar_log("prestamo", f"libro {isbn} a socio {id_socio}")

    def devolver_libro(self, id_socio):
        socio = self.buscar_socio(id_socio)

        if socio is None:
            raise ValueError("no existe ese socio")
        if not socio.tiene_libro():
            raise ValueError("el socio no tiene ningun libro")
        isbn = socio.isbn_prestado
        libro = self.buscar_libro(isbn)
        libro.id_socio = None
        socio.isbn_prestado = None
        registrar_log("devolucion", f"libro {isbn} de socio {id_socio}")

    def anadir_libro(self, isbn, titulo, autor, anio, categoria):
        if self.buscar_libro(isbn) is not None:
            raise ValueError("ya existe un libro con ese codigo")
        self.libros.append(Libro(isbn, titulo, autor, anio, categoria, None))
        registrar_log("libro anadido", f"{isbn} - {titulo}")

    def anadir_socio(self, id_socio, nombre, email):
        if self.buscar_socio(id_socio) is not None:
            raise ValueError("ya existe un socio con ese codigo")
        self.socios.append(Socio(id_socio, nombre, email, None))
        registrar_log("socio anadido", f"{id_socio} - {nombre}")

    def guardar(self):
        guardar_libros(self.libros)
        guardar_socios(self.socios)