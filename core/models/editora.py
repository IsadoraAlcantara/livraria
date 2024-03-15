from django.db import models


class Editora(models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField(max_length=200, blank=True, null=True)
    # entrada de dados blank=True não obrigatório
    # banco null=True não obrigatório

    def __str__(self):
        return f"{self.nome} ({self.id})"
