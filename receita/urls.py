from django.urls import path, include
from receita.api.viewsets import ReceitaViewSet
from rest_framework.routers import DefaultRouter

"""
No arquivo urls.py esta sendo registrado as rotas da api rest referente a classe Receita;
"""

router = DefaultRouter()
router.register('', ReceitaViewSet)


urlpatterns = [
    path('', include(router.urls))
]