class Libro:
    def __init__(self, isbn, titulo, autor, anio, categoria, id_socio):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.categoria = categoria
        self.id_socio = None

    def __str__(self):
        return f"Libro: {self.titulo} | ISBN: {self.isbn} | autor: {self.autor} | fecha de publicación: {self.anio} | categoria: {self.categoria}"

    def esta_disponible(self):
        return self.id_socio == None
