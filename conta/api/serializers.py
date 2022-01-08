from rest_framework.serializers import ModelSerializer
from conta.models import Conta

class ContaSerializer(ModelSerializer):
    class Meta:
        model = Conta
        fields = "__all__"

