from django.shortcuts import render
from rest_framework.decorators import api_view
from conta.models import Conta
# Create your views here.

@api_view(['GET'])
def listar_contas(request):
    conta = Conta.objects.all()
    return render(request,"conta/listar_contas.html",{"contas":conta})







