from django.db import models
from django.utils import timezone

PROVINCIAS = (
    ("Maputo Provincia ", "Maputo Provincia"),
    ("Maputo Cidade", "Maputo Cidade"),
    ("Gaza", "Gaza"),
    ("Inhambane", "Inhambane"),
    ("Sofala", "Sofala"),
    ("Manica", "Manica"),
    ("Tete", "Tete"),
    ("Zambezia", "Zambezia"),
    ("Nampula", "Nampula"),
    ("Cabo Delgado","Cabo Delgado"),
    ("Niassa", "Niassa")
)

REUNIAO = (
    ("Sexta-Feira", "Sexta-Feira"),
    ("Domingo", "Domingo")
)

class Plataforma(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Igreja(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    provincia = models.CharField(max_length=30, choices=PROVINCIAS)
    bairro = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return self.nome

class Relatorio(models.Model):
    igreja = models.ForeignKey(Igreja, on_delete=models.SET_NULL, blank=True, null=True)
    data_reuniao = models.DateField(default=timezone.now)
    familia = models.CharField(max_length=100)
    membros = models.IntegerField()
    bairro = models.CharField(max_length=255)
    contacto = models.CharField(max_length=50)
    plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE)
    reuniao = models.CharField(max_length=20, choices=REUNIAO)

    def __str__(self):
        return self.familia

