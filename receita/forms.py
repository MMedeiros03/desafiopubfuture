from django import forms
from django.forms.models import ModelForm
from conta.models import Conta
from .models import TIPORECEITA, Receita


class Receita_Form(ModelForm):
    class Meta:
        model = Receita
        fields = "__all__"

class ReceitaForm(forms.Form):
    valor = forms.DecimalField(max_digits=9,decimal_places=2)
    dataRecebimento = forms.DateField()
    dataRecebimentoEsperado = forms.DateField()
    descricao = forms.CharField(max_length=250)
    conta = forms.ModelChoiceField(queryset=Conta.objects.all())
    tipoReceita = forms.CharField(
        max_length=8,
        widget=forms.Select(choices=TIPORECEITA),
    )




