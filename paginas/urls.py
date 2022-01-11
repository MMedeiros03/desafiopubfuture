from django.urls import path
from conta.views import listar_contas,conta,cadastrar_contas,excluir_conta,detalhes_conta
from django.views.generic import RedirectView
from .views import PaginaPrincipal
app_name = "paginas"

urlpatterns = [
    path('contas/',listar_contas, name = "contas"),
    path("contas/<int:id>/",detalhes_conta,name="detalhes_conta"),
    path('contas/conta/',conta, name="conta"),
    path('contas/conta/submit',cadastrar_contas, name="submit"),
    path('contas/conta/delete/<int:id_conta>',excluir_conta, name="delete"),
    path("",RedirectView.as_view(url="home/")),
    path('home/',PaginaPrincipal.as_view(), name="home"),
]