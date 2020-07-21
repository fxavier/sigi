from . views import IndexTemplateView, RelatorioListView, RelatorioCreateView
from django.urls import path


app_name = 'core'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name="index"),
    path('relatorio/novo', RelatorioCreateView.as_view(), name="criar_relatorio"),
    path('relatorios/', RelatorioListView.as_view(), name="relatorios"),
]