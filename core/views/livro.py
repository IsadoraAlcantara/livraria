from rest_framework.viewsets import ModelViewSet

from core.models import Livro
from core.serializers import LivroDetailSerializer, LivroListSerializer, LivroSerializer


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    # queryset = Livro.objects.order_by("titulo") ordernando alfabeticamente pelo título
    serializer_class = LivroSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return LivroListSerializer  # listagem menor (poucos detalhes)
        elif self.action == "retrieve":
            return LivroDetailSerializer  # listagem maior (todos os detalhes)
        return LivroSerializer
