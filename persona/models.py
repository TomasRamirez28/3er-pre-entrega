from django.db import models

# Create your models here.
# class Auto(models.Model):
#     modelo = models.CharField(max_length=20)
#     marca = models.CharField(max_length=20)
    
#     def __str__(self):
#         return f"Soy el auto { self.modelo} {self.marca}"
 
class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    email = models.EmailField()
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"