from django.urls import path, include
from rest_framework.routers import DefaultRouter
from despesa.api.viewsets import DespesaViewSet

router = DefaultRouter()
router.register('', DespesaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]