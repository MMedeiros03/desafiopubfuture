from django.shortcuts import render,redirect,get_object_or_404
from rest_framework.decorators import api_view
from .models import Receita

# Create your views here.

@api_view(['GET'])
def listar_receitas(request):
    receita = Receita.objects.all()
    return render(request,"receita/listar_receitas.html",{"receitas":receita})

def detalhes_receita(request,id=None,*args,**kwargs):
    receita = get_object_or_404(Receita,id = id)
    return render(request,"receita/detalhes_receita.html",{"receita":receita})


def receita(request):
    id_receita = request.GET.get('id')
    dados = {}
    if id_receita:
        dados['receita'] = Receita.objects.get(id=id_receita)
    return render(request,"receita/cadastrar_receita.html",dados)

def cadastrar_receitas(request):
    if request.POST:
        valor = request.POST.get("valor")
        dataRecebimento = request.POST.get("dataRecebimento")
        dataRecebimentoEsperado = request.POST.get("dataRecebimentoEsperado")
        descricao = request.POST.get("descricao")
        tipoReceita = request.POST.get("tipoReceita")
        conta = request.POST.get("conta")
        id_receita = request.POST.get("id_receita")
        if id_receita:
            Receita.objects.filter(id=id_receita).update(valor = valor,
                                                        dataRecebimento = dataRecebimento,
                                                        dataRecebimentoEsperado = dataRecebimentoEsperado,
                                                        descricao = descricao,
                                                        tipoReceita = tipoReceita,
                                                        conta = conta)
        else:
            Receita.objects.create(
                                valor = valor,
                                dataRecebimento = dataRecebimento,
                                dataRecebimentoEsperado = dataRecebimentoEsperado,                                                descricao = descricao,
                                tipoReceita = tipoReceita,
                                conta = conta)
    return redirect("/")


def excluir_receita(request,id_receita):
    Receita.objects.filter(id=id_receita).delete()
    return redirect("/")











