from rest_framework import viewsets
from despesa.models import Despesa
from despesa.api.serializers import DespesaSerializer

class DespesaViewSet(viewsets.ModelViewSet):
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer

