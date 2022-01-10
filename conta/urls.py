from django.urls import path, include
from conta.api.viewsets import ContaViewSet
from rest_framework.routers import DefaultRouter
from django.views.generic import RedirectView
from .views import conta,cadastrar_contas,listar_contas


router = DefaultRouter()
router.register('', ContaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
