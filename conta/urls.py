from django.urls import path, include
from conta.api.viewsets import ContaViewSet
from rest_framework.routers import DefaultRouter

"""
No arquivo urls.py esta sendo registrado as rotas da api rest referente a classe Conta;
"""

router = DefaultRouter()
router.register('', ContaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
