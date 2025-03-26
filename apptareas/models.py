from django.db import models

# Create your models here.


class Tareas(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    completado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre 
