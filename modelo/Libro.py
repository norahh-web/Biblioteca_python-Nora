class Libro:
    def __init__(self, isbn, titulo, autor, anio, categoria):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.categoria = categoria

    def __str__(self):
        return f"Libro: {self.titulo} | ISBN: {self.isbn} | autor: {self.autor} | fecha de publicación: {self.anio} | categoria: {self.categoria}"
