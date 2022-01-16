from django.shortcuts import render,redirect,get_object_or_404
from rest_framework.decorators import api_view
from .models import Receita
from .forms import Receita_Form

# Create your views here.

@api_view(['GET'])
def listar_receitas(request):
    receita = Receita.objects.all()
    qtde_receita = len(receita)
    return render(request,"receita/listar_receitas.html",{"receitas":receita,"qtde":qtde_receita})

def detalhes_receita(request,id=None,*args,**kwargs):
    receita = get_object_or_404(Receita,id = id)
    return render(request,"receita/detalhes_receita.html",{"receita":receita})

def receita(request):
    if request.method == "GET":
        form = Receita_Form()
        context = {
            'form':form
        }
        return render(request,"receita/cadastrar_receita.html",context=context)
    else: 
        form = Receita_Form(request.POST)
        if form.is_valid():
            receita = form.save()
            form = Receita_Form()
        context = {
        'form':form
            }      
        return render(request,"receita/cadastrar_receita.html",context=context)
            
def editar_receita(request,id_receita):
    if request.method == "GET":
        receita = Receita.objects.filter(id=id_receita).first()
        form = Receita_Form(instance=receita)
        context = {
            'form':form,
        }
        return render(request,"receita/cadastrar_receita.html",context=context)

    elif request.method == "POST":
        receita = Receita.objects.filter(id=id_receita).first()
        form = Receita_Form(request.POST,instance=receita)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            context = {
            'form':form,
            }      
            return render(request,"receita/cadastrar_receita.html",context=context)

def excluir_receita(request,id_receita):
    Receita.objects.filter(id=id_receita).delete()
    return redirect("/")












