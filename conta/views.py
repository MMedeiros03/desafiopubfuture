from http.client import HTTPResponse
from turtle import circle
from django.shortcuts import render,redirect,get_object_or_404
from rest_framework.decorators import api_view
from conta.models import Conta

# Create your views here.

@api_view(['GET'])
def listar_contas(request):
    conta = Conta.objects.all()
    return render(request,"conta/listar_contas.html",{"contas":conta})

def detalhes_conta(request,id=None,*args,**kwargs):
    conta = get_object_or_404(Conta,id = id)
    return render(request,"conta/detalhes_contas.html",{"conta":conta})


def conta(request):
    id_conta = request.GET.get('id')
    dados = {}
    if id_conta:
        dados['conta'] = Conta.objects.get(id=id_conta)
    return render(request,"conta/cadastrar_contas.html",dados)

def cadastrar_contas(request):
    if request.POST:
        numConta = request.POST.get("numConta")
        saldo = request.POST.get("saldo")
        tipoConta = request.POST.get("tipoConta")
        instituicaoFinanceira = request.POST.get("instituicaoFinanceira")
        id_conta = request.POST.get("id_conta")
        if id_conta:
            Conta.objects.filter(id=id_conta).update(numConta=numConta,
                                                    saldo=saldo,
                                                    tipoConta=tipoConta,
                                                    instituicaoFinanceira=instituicaoFinanceira)
        else:
            Conta.objects.create(
                                numConta=numConta,
                                saldo=saldo,
                                tipoConta=tipoConta,
                                instituicaoFinanceira=instituicaoFinanceira)
    return redirect("/")


def excluir_conta(request,id_conta):
    Conta.objects.filter(id=id_conta).delete()
    return redirect("/")


def saldo_total(request):
    contas = Conta.objects.all(saldo)
    #saldo = contas.values().distinct()
    #list_saldo = list(saldo)
    #print("testando se a lista funcionou", list_saldo)
    print(contas)
    return render(request,"conta/saldo_total.html",{"contas":contas})#"saldo":saldo











