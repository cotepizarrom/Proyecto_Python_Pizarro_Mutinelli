from django.urls import path
from .views import PageListView, PageDetailView, PageCreateView

urlpatterns = [
    path('', PageListView.as_view(), name='page_list'),
    path('<int:pk>/', PageDetailView.as_view(), name='page_detail'),
    path('new/', PageCreateView.as_view(), name='page_create'),   # <— NUEVO
]

from .views import PageListView, PageDetailView, PageCreateView, PageUpdateView

urlpatterns = [
    path('', PageListView.as_view(), name='page_list'),
    path('new/', PageCreateView.as_view(), name='page_create'),       # primero rutas de texto
    path('<int:pk>/', PageDetailView.as_view(), name='page_detail'),  # luego las numéricas
    path('<int:pk>/edit/', PageUpdateView.as_view(), name='page_update'),
]

from .views import (
    PageListView, PageDetailView, PageCreateView,
    PageUpdateView, PageDeleteView
)

urlpatterns = [
    path('', PageListView.as_view(), name='page_list'),
    path('new/', PageCreateView.as_view(), name='page_create'),
    path('<int:pk>/', PageDetailView.as_view(), name='page_detail'),
    path('<int:pk>/edit/', PageUpdateView.as_view(), name='page_update'),
    path('<int:pk>/delete/', PageDeleteView.as_view(), name='page_delete'),  # <- NUEVO
]