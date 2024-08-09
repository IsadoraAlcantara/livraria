from rest_framework.viewsets import ModelViewSet

from core.models import Livro
from core.serializers import LivroSerializer, LivroDetailSerializer


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    # queryset = Livro.objects.order_by("titulo") ordernando alfabeticamente pelo título
    serializer_class = LivroSerializer

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return LivroDetailSerializer
        return LivroSerializer