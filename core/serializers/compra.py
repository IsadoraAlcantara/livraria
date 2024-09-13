from rest_framework.serializers import CharField, ModelSerializer

from core.models import Compra, ItensCompra

class ItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = "__all__"

class CompraSerializer(ModelSerializer):
    usuario = CharField(source="usuario.email", read_only=True) # lê o email invés do id na api
    status = CharField(source="get_status_display", read_only=True) # muda o status da compra pra o texto invés do número
    itens = ItensCompraSerializer(many=True, read_only=True)

    class Meta:
        model = Compra
        fields = "__all__"