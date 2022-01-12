from rest_framework.serializers import ModelSerializer
from despesa.models import Despesa

class DespesaSerializer(ModelSerializer):
    class Meta:
        model = Despesa
        fields = "__all__"
