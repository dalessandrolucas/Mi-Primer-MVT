from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre=models.CharField(max_length=50)
    edad=models.IntegerField()
    fecha_nacimiento=models.DateField()


    def datos(self):
        return f"Me llamo {self.nombre}, tengo {self.edad} anios y nací el {self.fecha_nacimiento}"
