from unicodedata import name
from django.urls import path
# conta
from conta.views import listar_contas,conta,cadastrar_contas,excluir_conta,detalhes_conta,saldo_total
# despesa
from despesa.views import listar_despesas,despesa,detalhes_despesa,excluir_despesa,editar_despesa
from django.views.generic import RedirectView
# receita
from receita.views import listar_receitas,detalhes_receita,excluir_receita,receita,editar_receita
from .views import PaginaPrincipal
app_name = "paginas"

urlpatterns = [
    # ----------Contas----------
    path('contas/',listar_contas, name = "contas"),
    path("contas/<int:id>/",detalhes_conta,name="detalhes_conta"),
    path('contas/conta/',conta, name="conta"),
    path('contas/conta/submit',cadastrar_contas, name="submit"),
    path('contas/conta/delete/<int:id_conta>',excluir_conta, name="delete"),
    path('saldo_total/',saldo_total,name="saldo_total"),
    # ----------Contas----------

    # ----------Despesas----------
    path("despesas/",listar_despesas,name="despesas"),
    path("despesas/<int:id>/",detalhes_despesa,name="detalhes_despesa"),
    path('despesas/despesa/',despesa, name="despesa"),
    path('despesas/editar/<int:id_despesa>/',editar_despesa,name="editar"),
    path('despesas/despesa/delete/<int:id_despesa>',excluir_despesa, name="delete"),

    # ----------Despesas----------

    # ----------Receitas----------
    path("receitas/",listar_receitas,name="receitas"),
    path("receitas/<int:id>/",detalhes_receita,name="detalhes_receita"),
    path('receitas/receita/',receita, name="receita"),
    path('receitas/editar/<int:id_receita>/',editar_receita,name="editar"),
    path('receitas/receita/delete/<int:id_receita>',excluir_receita, name="delete"),

    # ----------Receitas----------
    path("",RedirectView.as_view(url="home/")),
    path('home/',PaginaPrincipal.as_view(), name="home"),
]