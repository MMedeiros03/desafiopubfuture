from django.shortcuts import render,redirect,get_object_or_404
from rest_framework.decorators import api_view
from .models import Despesa
from .forms import Despesa_Form
# Create your views here.

@api_view(['GET'])
def listar_despesas(request):
    despesa = Despesa.objects.all()
    return render(request,"despesa/listar_despesas.html",{"despesas":despesa})

def detalhes_despesa(request,id=None,*args,**kwargs):
    despesa = get_object_or_404(Despesa,id = id)
    return render(request,"despesa/detalhes_despesa.html",{"despesa":despesa})


def despesa(request):
    if request.method == "GET":
        form = Despesa_Form()
        context = {
            'form':form
        }
        return render(request,"despesa/cadastrar_despesa.html",context=context)
    else: 
        form = Despesa_Form(request.POST)
        if form.is_valid():
            despesa = form.save()
            form = Despesa_Form()
        context = {
        'form':form
            }      
        return render(request,"despesa/cadastrar_despesa.html",context=context)
"""
def cadastrar_despesa(request):
    if request.POST:
        valor = request.POST.get("valor")
        dataPagamento = request.POST.get("dataPagamento")
        dataPagamentoEsperado = request.POST.get("dataPagamentoEsperado")
        tipoDespesa = request.POST.get("tipoDespesa")
        conta = request.POST.get("conta")
        id_despesa = request.POST.get("id_despesa")
        if id_despesa:
            Despesa.objects.filter(id=id_despesa).update(valor=valor,
                                                         dataPagamento=dataPagamento,
                                                         dataPagamentoEsperado=dataPagamentoEsperado,
                                                         tipoDespesa=tipoDespesa,
                                                         conta=conta)
        else:
            Despesa.objects.create(
                                valor=valor,
                                dataPagamento=dataPagamento,
                                dataPagamentoEsperado=dataPagamentoEsperado,
                                tipoDespesa=tipoDespesa,
                                conta=conta)
    return redirect("/")
"""

def excluir_despesa(request,id_despesa):
    Despesa.objects.filter(id=id_despesa).delete()
    return redirect("/")
