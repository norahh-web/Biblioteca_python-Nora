from controlador.almacenamiento import cargar_libros, cargar_socios, registrar_log

libros = cargar_libros()
socios = cargar_socios()

print(len(libros), len(socios))
print(libros[0])
print(socios[0])
print(libros[0].id_socio)
print(libros[1].id_socio)
print(socios[0].isbn_prestado)
print(socios[1].isbn_prestado)

registrar_log("prueba", "probando el log")