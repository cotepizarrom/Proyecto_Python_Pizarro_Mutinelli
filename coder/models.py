from django.db import models

class Cliente(models.Model):
    nombre_empresa = models.CharField(max_length=150)
    rut = models.CharField(max_length=15, unique=True)
    nombre_contacto = models.CharField(max_length=100)
    email_contacto = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True)
    fecha_ingreso = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre_empresa} - {self.nombre_contacto}"


class Servicio(models.Model):
    TIPO_CHOICES = [
        ("CONT", "Contabilidad"),
        ("CG", "Control de Gestión"),
        ("PAY", "Payroll"),
        ("LEGAL", "Legal/Laboral"),
        ("CFO", "CFO as a Service"),
    ]
    nombre = models.CharField(max_length=50, choices=TIPO_CHOICES)
    descripcion = models.TextField(blank=True)
    precio_base_mensual = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return self.get_nombre_display()


class Lead(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    empresa = models.CharField(max_length=150, blank=True)
    servicio_interes = models.ForeignKey(Servicio, on_delete=models.SET_NULL, null=True)
    comentarios = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=20,
        choices=[("nuevo", "Nuevo"), ("contactado", "Contactado"), ("cerrado", "Cerrado")],
        default="nuevo",
    )

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.servicio_interes}"
