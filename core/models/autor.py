from django.db import models 

class Autor(models.Model):
    nome = models.CharField(max_length=100),
    email = models.EmailField(max_length=200, blank=True, null=True)

    def _str_(self):
        return f"{self.nome}, ({self.id})"
