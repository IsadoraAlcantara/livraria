from rest_framework.serializers import CharField, ModelSerializer

from core.models import Compra

class CompraSerializer(ModelSerializer):
    usuario = CharField(source="usuario.email", read_only=True) # lê o email invés do id na api
    status = CharField(source="get_status_display", read_only=True) # muda o status da compra pra o texto invés do número

    class Meta:
        model = Compra
        fields = "(__all__)"