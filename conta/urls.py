from django.urls import path, include
from conta.api.viewsets import ContaViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', ContaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
