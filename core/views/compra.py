from rest_framework.viewsets import ModelViewSet

from core.models import Compra
from core.serializers import (
    CompraSerializer,
    CriarEditarCompraSerializer,
    ListarCompraSerializer,
)


class CompraViewSet(ModelViewSet):
    # queryset = Compra.objects.order_by("-id")
    # serializer_class = CompraSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return ListarCompraSerializer
        if self.action in ("create", "update"):
            return CriarEditarCompraSerializer
        return CompraSerializer

    def get_queryset(self):
        usuario = self.request.user
        if usuario.is_superuser:
            return Compra.objects.order_by("-id")
        if usuario.groups.filter(name="Administradores"):
            return Compra.objects.order_by("-id")
        return Compra.objects.filter(usuario=usuario).order_by("-id")