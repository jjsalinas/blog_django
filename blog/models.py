from django.db import models
from django.utils import timezone

class Entrada(models.Model):
    autor = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=200)
    cuerpo = models.TextField()
    fecha_crea = models.DateTimeField(default=timezone.now)
    fecha_publi = models.DateTimeField(blank=True, null=True)

    def publica(self):
        self.fecha_publi = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
        