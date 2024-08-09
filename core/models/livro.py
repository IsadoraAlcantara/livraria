from django.db import models

from.categoria import Categoria
from.editora import Editora
from.autor import Autor


class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length=32, null=True, blank=True)
    quantidade = models.IntegerField(default=0, blank=True, null=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="livros", blank=True, null=True)
    editora = models.ForeignKey(Editora, on_delete=models.PROTECT, related_name="livros", blank=True, null=True)
    autor = models.ManyToManyField(Autor, related_name="livros", blank=True, null=True) # livro n:n autor
    # autor = models.ForeignKey(Autor, on_delete=models.PROTECT, related_name="livrosAutor", blank=True, null=True) livro 1:n autor
    # coautor = models.ForeignKey(Autor, on_delete=models.PROTECT, related_name="livrosCoautor", blank=True, null=True) livro 1:n coautor

    def __str__(self):
        return f"({self.id}) {self.titulo} ({self.quantidade})"