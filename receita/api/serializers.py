"""
from inspect import ClassFoundException
from django.db import models
from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from atracoes.models import Atracao

class AtracaoSerializer(ModelSerializer):
    class Meta:
        model = Atracao
        fields = ("id",'nome','descricao','horario_func','idade_minima')
"""