from errores.libro_no_disponible import LibroNoDisponibleError

class Menu:
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

    def mostrar_opciones(self):
        print()
        print("1. Mostrar todos los libros")
        print("2. Mostrar libros disponibles")
        print("3. Buscar libro por titulo")
        print("4. Prestar libro")
        print("5. Devolver libro")
        print("6. Socios con libro")
        print("7. Añadir libro o socio")
        print("8. Salir")

    def ejecutar(self):
        opcion = ""
        while opcion != "8":
            self.mostrar_opciones()
            opcion = input("opcion: ")
            if opcion == "1":
                self.mostrar_libros()
            elif opcion == "2":
                self.mostrar_disponibles()
            elif opcion == "3":
                self.buscar_titulo()
            elif opcion == "4":
                self.prestar()
            elif opcion == "5":
                self.devolver()
            elif opcion == "6":
                self.mostrar_socios_con_libro()
            elif opcion == "7":
                self.anadir()
            elif opcion == "8":
                self.biblioteca.guardar()
                print("datos guardados, hasta pronto")
            else:
                print("opcion no valida")

    # Métodos del menú

    def mostrar_libros(self):
        #1
        for libro in self.biblioteca.libros:
            print(libro)

    def mostrar_disponibles(self):
        #2
        for libro in self.biblioteca.libros_disponibles():
            print(libro)

    def buscar_titulo(self):
        #3
        texto = input("título o parte del titulo: ")
        encontrados = self.biblioteca.buscar_por_titulo(texto)
        if len(encontrados) == 0:
            print("no existe ningun libro con ese titulo")
        for libro in encontrados:
            print(libro)

    def prestar(self):
        #4
        isbn = input("isbn: ")
        id_socio = input("código del socio: ")
        try:
            self.biblioteca.prestar_libro(isbn, id_socio)
        # Captura el error en caso de que el libro ya esté prestado por otro socio:
        except LibroNoDisponibleError as e:
            print(e, "- libro:", e.isbn)
        except ValueError as e:
            print(e)
        else:
            print("prestamo realizado")

    def devolver(self):
        #5
        id_socio = input("codigo del socio: ")
        try:
            self.biblioteca.devolver_libro(id_socio)
        except ValueError as e:
            print(e)
        else:
            print("libro devuelto")

    def mostrar_socios_con_libro(self):
        #6
        socios = self.biblioteca.socios_con_libro()
        if len(socios) == 0:
            print("ningun socio tiene libros")
        for socio in socios:
            libro = self.biblioteca.buscar_libro(socio.isbn_prestado)
            print(socio.nombre, "->", libro.titulo)

    def anadir(self):
        #7
        tipo = input("1 = libro, 2 = socio: ")
        try:
            if tipo == "1":
                isbn = input("codigo: ")
                titulo = input("titulo: ")
                autor = input("autor: ")
                anio = int(input("año: "))
                categoria = input("categoria: ")
                self.biblioteca.anadir_libro(isbn, titulo, autor, anio, categoria)
            elif tipo == "2":
                id_socio = input("codigo: ")
                nombre = input("nombre: ")
                email = input("email: ")
                self.biblioteca.anadir_socio(id_socio, nombre, email)
            else:
                print("opcion no valida")
                return
        except ValueError as e:
            print(e)
        else:
            print("anadido correctamente")