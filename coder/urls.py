from django.urls import path
from .views import home, cliente_create, servicio_create, lead_create, cliente_search

urlpatterns = [
    path("", home, name="home"),
    path("clientes/nuevo/", cliente_create, name="cliente_create"),
    path("servicios/nuevo/", servicio_create, name="servicio_create"),
    path("leads/nuevo/", lead_create, name="lead_create"),
    path("clientes/buscar/", cliente_search, name="cliente_search"),
]

from django.urls import path, include
# ...
path('accounts/', include('accounts.urls')),