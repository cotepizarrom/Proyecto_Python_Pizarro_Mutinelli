from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from .forms import ClienteForm, ServicioForm, LeadForm, ClienteSearchForm
from .models import Cliente

def home(request):
    return render(request, "coder/base.html")

def cliente_create(request):
    form = ClienteForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Cliente creado correctamente.")
        return redirect("cliente_create")
    return render(request, "coder/cliente_form.html", {"form": form})

def servicio_create(request):
    form = ServicioForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Servicio creado correctamente.")
        return redirect("servicio_create")
    return render(request, "coder/servicio_form.html", {"form": form})

def lead_create(request):
    form = LeadForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "¡Gracias! Recibimos tus datos y te contactaremos pronto.")
        return redirect("lead_create")
    return render(request, "coder/lead_form.html", {"form": form})

def cliente_search(request):
    form = ClienteSearchForm(request.GET or None)
    resultados = []
    if form.is_valid():
        q = form.cleaned_data.get("q", "").strip()
        if q:
            resultados = Cliente.objects.filter(
                Q(nombre_empresa__icontains=q) |
                Q(rut__icontains=q) |
                Q(nombre_contacto__icontains=q)
            ).order_by("nombre_empresa")
    return render(request, "coder/cliente_search.html", {"form": form, "resultados": resultados})
