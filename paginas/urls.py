from django.urls import path
from conta.views import listar_contas,conta,cadastrar_contas,excluir_conta
from django.views.generic import RedirectView

app_name = "paginas"

urlpatterns = [
    path('contas/',listar_contas, name = "contas"),
    path('contas/conta/',conta, name="conta"),
    path('contas/conta/submit',cadastrar_contas, name="submit"),
    path('contas/conta/delete/<int:id_conta>',excluir_conta, name="delete"),
    path('home/',RedirectView.as_view(url="contas/")),
]