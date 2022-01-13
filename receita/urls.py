from django.urls import path, include
from receita.api.viewsets import ReceitaViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', ReceitaViewSet)


urlpatterns = [
    path('', include(router.urls))
]