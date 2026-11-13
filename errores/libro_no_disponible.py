class LibroNoDisponibleError(Exception):
    def __init__(self, mensaje, isbn):
        super().__init__(mensaje)
        self.isbn = isbn