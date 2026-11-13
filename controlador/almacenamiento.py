from datetime import datetime
from modelo.Libro import Libro
from modelo.Socio import Socio

RUTA_LIBROS = "datos/libros.txt"
RUTA_SOCIOS = "datos/socios.txt"
RUTA_LOG = "datos/log.txt"

def cargar_libros():
    libros = []
    with open(RUTA_LIBROS, "r", encoding="utf-8") as f:
        for linea in f:
            if linea.strip() == "":
                continue
            partes = linea.strip().split(";")
            id_socio = partes[5]
            if id_socio == "None":
                id_socio = None
            libros.append(Libro(partes[0], partes[1], partes[2], int(partes[3]), partes[4], id_socio))
    return libros

def cargar_socios():
    socios = []
    with open(RUTA_SOCIOS, "r", encoding="utf-8") as f:
        for linea in f:
            if linea.strip() == "":
                continue
            partes = linea.strip().split(";")
            isbn = partes[3]
            if isbn == "None":
                isbn = None
            socios.append(Socio(partes[0], partes[1], partes[2], isbn))
    return socios

def guardar_libros(libros):
    with open(RUTA_LIBROS, "w", encoding="utf-8") as f:
        for libro in libros:
            f.write(f"{libro.isbn};{libro.titulo};{libro.autor};{libro.anio};{libro.categoria};{libro.id_socio}\n")

def guardar_socios(socios):
    with open(RUTA_SOCIOS, "w", encoding="utf-8") as f:
        for socio in socios:
            f.write(f"{socio.id_socio};{socio.nombre};{socio.email};{socio.isbn_prestado}\n")

def registrar_log(evento, detalles):
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open(RUTA_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{fecha}][{evento}][{detalles}]\n")