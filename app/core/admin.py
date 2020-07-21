from django.contrib import admin

from . models import Plataforma, Igreja, Relatorio



class RelatorioAdmin(admin.ModelAdmin):
    list_display = ['igreja','data_reuniao', 'familia', 'membros', 'bairro', 'contacto', 'plataforma', 'reuniao']


admin.site.register(Plataforma)
admin.site.register(Igreja)
admin.site.register(Relatorio, RelatorioAdmin)

admin.site.site_header =('Gestao de Reunioes')