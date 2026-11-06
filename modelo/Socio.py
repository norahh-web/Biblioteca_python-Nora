class Socio: 
   def __init__(self, id_socio, nombre, email):
       self.id_socio = id_socio
       self.nombre = nombre
       self.email = email

   def __str__(self):
       return f"Nombre del socio: {self.nombre} - ID: {self.id_socio} - correo electrónico: {self.email}"