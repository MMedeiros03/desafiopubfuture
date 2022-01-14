from django import forms
from django.forms.models import ModelForm
from conta.models import Conta
from .models import TIPODESPESA, Despesa


class Despesa_Form(ModelForm):
    class Meta:
        model = Despesa
        fields = "__all__"

class DespesaForm(forms.Form):
    valor = forms.DecimalField(max_digits=9,decimal_places=2)
    dataPagamento = forms.DateField()
    dataPagamentoEsperado = forms.DateField()
    conta = forms.ModelChoiceField(queryset=Conta.objects.all())
    tipoDespesa = forms.CharField(
        max_length=8,
        widget=forms.Select(choices=TIPODESPESA),
    )




