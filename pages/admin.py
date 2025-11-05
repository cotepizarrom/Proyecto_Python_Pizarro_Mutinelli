from django.contrib import admin
from .models import Page

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo', 'fecha_publicacion', 'creado', 'actualizado')
    search_fields = ('titulo', 'subtitulo', 'contenido')
    list_filter = ('fecha_publicacion', 'creado')
    ordering = ('-fecha_publicacion',)