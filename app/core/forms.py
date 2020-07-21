from . models import Relatorio, Igreja, Plataforma
from django import forms


class InsereRelatorioForm(forms.ModelForm):

    class Meta:
        model = Relatorio

        fields = ['igreja',
                 'data_reuniao',
                 'familia',
                 'membros',
                 'bairro',
                 'contacto',
                 'plataforma',
                 'reuniao'
        ]