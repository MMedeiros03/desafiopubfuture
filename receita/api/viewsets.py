from rest_framework import viewsets
from receita.models import Receita
from receita.api.serializers import ReceitaSerializer

class ReceitaViewSet(viewsets.ModelViewSet):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer

