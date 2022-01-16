from django.urls import path, include
from rest_framework.routers import DefaultRouter
from despesa.api.viewsets import DespesaViewSet

"""
No arquivo urls.py esta sendo registrado as rotas da api rest referente a classe Despesa;
"""

router = DefaultRouter()
router.register('', DespesaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]