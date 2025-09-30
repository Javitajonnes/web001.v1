from django.db import models

class Noticia(models.Model):
    titulo=models.CharField(max_length=100)
    detalle=models.TextField()
    imagen=models.ImageField(upload_to='noticias/', blank=True, null=True)

    def __str__(self):
        return self.titulo
    
class Replica(models.Model):
    name=models.CharField(max_length=50)
    detalle=models.TextField()
    numero=models.SmallIntegerField()

    def __str__(self):
            return self.name