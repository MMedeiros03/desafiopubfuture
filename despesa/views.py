from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from conta.models import Conta

# Create your views here.

@api_view(['GET'])
def listar_contas(request):
    conta = Conta.objects.all()
    return render(request,"base/home.html",{"contas":conta})

def conta(request):
    id_conta = request.GET.get('id_conta')
    dados = {}
    if id_conta:
        dados['conta'] = Conta.objects.get(id=id_conta)
    return render(request,"conta/cadastrar_conta.html",dados)

def cadastrar_contas(request):
    if request.POST:
        numConta = request.POST.get("numConta")
        saldo = request.POST.get("saldo")
        tipoConta = request.POST.get("tipoConta")
        instituicaoFinanceira = request.POST.get("instituicaoFinanceira")
        id_conta = request.POST.get("id_conta")
        if id_conta is False:
            Conta.objects.create(id = id_conta,
                                numConta=numConta,
                                saldo=saldo,
                                tipoConta=tipoConta,
                                instituicaoFinanceira=instituicaoFinanceira)
    return redirect("/")


def editar_conta(request):
    if request.POST:
        numConta = request.POST.get("numConta")
        saldo = request.POST.get("saldo")
        tipoConta = request.POST.get("tipoConta")
        instituicaoFinanceira = request.POST.get("instituicaoFinanceira")
        id_conta = request.POST.get("id_conta")
        if id_conta:
            Conta.objects.filter(id=id_conta).update(tnumConta=numConta,
                                                    saldo=saldo,
                                                    tipoConta=tipoConta,
                                                    instituicaoFinanceira=instituicaoFinanceira)
    return redirect("/")

def excluir_conta(request,id):
    if Conta.id is True:
        Conta.delete()
    else:
        raise Http404()
    return redirect("/")
