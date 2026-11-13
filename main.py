from controlador.biblioteca import Biblioteca
from vista.menu import Menu

biblioteca = Biblioteca()
print("se han cargado", len(biblioteca.libros), "libros y", len(biblioteca.socios), "socios")
menu = Menu(biblioteca)
menu.ejecutar()