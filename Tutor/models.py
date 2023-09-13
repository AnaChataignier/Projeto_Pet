from django.db import models

class Tutor(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=150, null=False, blank=False, unique=True)
    telefone = models.IntegerField(null=False, blank=False)
    endereco = models.CharField(max_length=250, null=False, blank=False)
    
    def __str__(self):
        return f"Tutor : {self.nome}"