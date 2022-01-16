from django.shortcuts import render,redirect,get_object_or_404
from rest_framework.decorators import api_view
from .models import Despesa
from .forms import Despesa_Form
# Create your views here.

@api_view(['GET'])
def listar_despesas(request):
    despesa = Despesa.objects.all()
    qtde_despesa = len(despesa)
    return render(request,"despesa/listar_despesas.html",{"despesas":despesa,"qtde":qtde_despesa})

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

def editar_despesa(request,id_despesa):
    if request.method == "GET":
        despesa = Despesa.objects.filter(id=id_despesa).first()
        form = Despesa_Form(instance=despesa)
        context = {
            'form':form,
        }
        return render(request,"despesa/cadastrar_despesa.html",context=context)

    elif request.method == "POST":
        despesa = Despesa.objects.filter(id=id_despesa).first()
        form = Despesa_Form(request.POST,instance=despesa)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            context = {
            'form':form,
            }      
            return render(request,"despesa/cadastrar_despesa.html",context=context)



def excluir_despesa(request,id_despesa):
    Despesa.objects.filter(id=id_despesa).delete()
    return redirect("/")
