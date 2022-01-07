"""
from rest_framework import viewsets
from atracoes.models import Atracao
from atracoes.api.serializer import AtracaoSerializer

class AtracaoViewSet(viewsets.ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
"""
