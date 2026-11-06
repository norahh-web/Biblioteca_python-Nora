class LibroNoDisponibleError(Exception):
    def __init__(self, valor):
        super().__init__("Error: Libro no disponible.")
        self.valor = valor