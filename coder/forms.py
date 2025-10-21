from django import forms
from .models import Cliente, Servicio, Lead

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"
        widgets = {
            "nombre_empresa": forms.TextInput(attrs={"class": "form-control"}),
            "rut": forms.TextInput(attrs={"class": "form-control", "placeholder": "12.345.678-9"}),
            "nombre_contacto": forms.TextInput(attrs={"class": "form-control"}),
            "email_contacto": forms.EmailInput(attrs={"class": "form-control"}),
            "telefono": forms.TextInput(attrs={"class": "form-control"}),
        }

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = "__all__"
        widgets = {
            "nombre": forms.Select(attrs={"class": "form-select"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "precio_base_mensual": forms.NumberInput(attrs={"class": "form-control"}),
        }

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ["nombre", "apellido", "email", "empresa", "servicio_interes", "comentarios"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "apellido": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "empresa": forms.TextInput(attrs={"class": "form-control"}),
            "servicio_interes": forms.Select(attrs={"class": "form-select"}),
            "comentarios": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        }

class ClienteSearchForm(forms.Form):
    q = forms.CharField(
        label="Buscar cliente",
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre empresa, RUT o contacto"})
    )
