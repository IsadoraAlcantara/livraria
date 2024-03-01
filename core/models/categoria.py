from django.db import models
# sempre deixar duas linhas entre from e class
# cada class é uma tabela
class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    # para deixar com o nome invés do id no admin
    def __str__(self):
        return self.descricao