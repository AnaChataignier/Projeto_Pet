from django.db import models

from datetime import datetime
from Tutor.models import Tutor

class Pet(models.Model):

    OPCOES_CATEGORIA = [
        ("GATO","Gato"),
        ("CACHORRO","Cachorro"),
        ("PÁSSAROS","Pássaros"),
        ("OUTROS","Outros"),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    raca = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    idade = models.PositiveIntegerField( null=False, blank=False)
    cor = models.CharField(max_length=20,null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/",max_length=312, blank=True)
    publicada = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(default=datetime.now, blank=False)
    tutor = models.ForeignKey(Tutor, on_delete=models.SET_NULL,
        null=True,
        blank=False,)

    def __str__(self):
        return self.nome