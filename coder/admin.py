from django.contrib import admin
from .models import Cliente, Servicio, Lead

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre_empresa", "rut", "nombre_contacto", "email_contacto", "fecha_ingreso")
    search_fields = ("nombre_empresa", "rut", "nombre_contacto", "email_contacto")

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio_base_mensual")
    list_filter = ("nombre",)
    search_fields = ("descripcion",)

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "email", "empresa", "servicio", "estado", "fecha_creacion")
    list_filter = ("estado", "servicio_interes", "fecha_creacion")
    search_fields = ("nombre", "apellido", "email", "empresa")
    readonly_fields = ("fecha_creacion",)

    def servicio(self, obj):
        return obj.servicio_interes
    servicio.short_description = "Servicio"