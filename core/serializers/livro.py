from rest_framework.serializers import ModelSerializer

from core.models import Livro


class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1 # busca as fk, mostrando os atributos das fk no json