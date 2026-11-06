class Socio: 
   def __init__(self, id_socio, nombre, email, isbn_prestado):
       self.id_socio = id_socio
       self.nombre = nombre
       self.email = email
       self.isbn_prestado = None

   def __str__(self):
       return f"Nombre del socio: {self.nombre} - ID: {self.id_socio} - correo electrónico: {self.email}"

   def tiene_libro(self):
       return self.isbn_prestado is not None