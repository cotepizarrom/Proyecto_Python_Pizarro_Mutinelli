from django.db import models
from ckeditor.fields import RichTextField

class Page(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=250, blank=True)
    contenido = RichTextField()  # texto con formato
    imagen = models.ImageField(upload_to='pages/', blank=True, null=True)
    fecha_publicacion = models.DateField()

    # Estos campos son opcionales, pero ayudan a ordenar
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-fecha_publicacion', '-creado']
        verbose_name = "Página"
        verbose_name_plural = "Páginas"

    def __str__(self):
        return self.titulo