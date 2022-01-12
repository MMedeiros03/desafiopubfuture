from django.urls import path
# conta
from conta.views import listar_contas,conta,cadastrar_contas,excluir_conta,detalhes_conta
# despesa
from despesa.views import cadastrar_despesa, listar_despesas,despesa,detalhes_despesa,excluir_despesa
from django.views.generic import RedirectView
from .views import PaginaPrincipal
app_name = "paginas"

urlpatterns = [
    # ----------Contas----------
    path('contas/',listar_contas, name = "contas"),
    path("contas/<int:id>/",detalhes_conta,name="detalhes_conta"),
    path('contas/conta/',conta, name="conta"),
    path('contas/conta/submit',cadastrar_contas, name="submit"),
    path('contas/conta/delete/<int:id_conta>',excluir_conta, name="delete"),
    # ----------Contas----------

    # ----------Despesas----------
    path("despesas/",listar_despesas,name="despesas"),
    path("despesas/<int:id>/",detalhes_despesa,name="detalhes_despesa"),
    path('despesas/despesa/',despesa, name="despesa"),
    path('despesas/despesa/submit',cadastrar_despesa, name="submit"),
    path('despesas/despesa/delete/<int:id_despesa>',excluir_despesa, name="delete"),

    # ----------Despesas----------
    path("",RedirectView.as_view(url="home/")),
    path('home/',PaginaPrincipal.as_view(), name="home"),
]