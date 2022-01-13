from rest_framework.serializers import ModelSerializer
from receita.models import Receita

class ReceitaSerializer(ModelSerializer):
    class Meta:
        model = Receita
        fields = "__all__"
