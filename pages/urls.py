from django.urls import path

from .views import pagina_principal 

app_name = "pages"

urlpatterns = [
    path("", pagina_principal, name="pagina_principal"),
    ]