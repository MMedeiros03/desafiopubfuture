from django.urls import path, include
from conta.api.viewsets import ContaViewSet
from rest_framework.routers import DefaultRouter
from .views import listar_contas

router = DefaultRouter()
router.register('', ContaViewSet)

urlpatterns = [
    path('lista/',listar_contas, name="listar_contas"),
    path('', include(router.urls)),
]