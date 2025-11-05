from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import Page
from .forms import PageForm
from django.db import models


class PageListView(ListView):
    model = Page
    template_name = 'pages/page_list.html'
    context_object_name = 'pages'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q', '').strip()
        if q:
            qs = qs.filter(
                models.Q(titulo__icontains=q) |
                models.Q(subtitulo__icontains=q)
            )
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['q'] = self.request.GET.get('q', '').strip()
        return ctx


class PageDetailView(DetailView):
    model = Page
    template_name = 'pages/page_detail.html'
    context_object_name = 'page'


class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    form_class = PageForm            # <- usa tu formulario con el widget
    template_name = 'pages/page_form.html'
    success_url = reverse_lazy('page_list')
    login_url = 'login'

    def form_valid(self, form):
        messages.success(self.request, "Página creada correctamente.")
        return super().form_valid(form)
    
from django.views.generic import UpdateView

class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name = 'pages/page_form.html'   # reutilizamos el mismo template
    success_url = reverse_lazy('page_list')
    login_url = 'login'

    def form_valid(self, form):
        messages.success(self.request, "Página actualizada correctamente.")
        return super().form_valid(form)
    
from django.views.generic import DeleteView

class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = 'pages/page_confirm_delete.html'  # plantilla de confirmación
    success_url = reverse_lazy('page_list')
    login_url = 'login'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Página eliminada correctamente.")
        return super().delete(request, *args, **kwargs)