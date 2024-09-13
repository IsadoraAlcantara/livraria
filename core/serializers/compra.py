from rest_framework.serializers import CharField, ModelSerializer, SerializerMethodField

from core.models import Compra, ItensCompra

class ItensCompraSerializer(ModelSerializer):
    total = SerializerMethodField()

    def get_total(self, instance):
        return instance.livro.preco * instance.quantidade

    class Meta:
        model = ItensCompra
        fields = ("livro", "quantidade", "total")
        depth = 1 # aparecer os detalhes - invés de apenas o id, aparece todas as infomações - quanto maior o número mais a fundo é a busca

class CompraSerializer(ModelSerializer):
    usuario = CharField(source="usuario.email", read_only=True) # lê o email invés do id na api
    status = CharField(source="get_status_display", read_only=True) # muda o status da compra pra o texto invés do número
    itens = ItensCompraSerializer(many=True, read_only=True)

    class Meta:
        model = Compra
        fields = "__all__"