from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView

from . models import Relatorio, Igreja, Plataforma
from . forms import InsereRelatorioForm


class IndexTemplateView(TemplateView):
    template_name = 'index.html'


class RelatorioListView(ListView):
    """Lista de Relatorios"""
    template_name = 'lista.html'
    model = Relatorio
    context_object_name = "relatorios"

class RelatorioCreateView(CreateView):
    """Criar um relatorio"""
    template_name = 'cria.html'
    model = Relatorio
    form_class = InsereRelatorioForm
    success_url = reverse_lazy("core:relatorios")
    
