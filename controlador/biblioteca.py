from modelo.Libro import Libro
from modelo.Socio import Socio

from errores.libro_no_disponible import LibroNoDisponibleError
from controlador.almacenamiento import cargar_libros, cargar_socios

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

        