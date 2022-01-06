from django.db import models
from django.db.models.fields import DateField, DecimalField, TextField
from conta.models import Conta
from django.urls import reverse 

# Create your models here.

class Receita(models.Model):
    valor = DecimalField(max_digits=9,decimal_places=2,blank=False,null=False)
    dataRecebimento = models.DateField(null=False,blank=False)
    dataPagamentoEsperado = models.DateField(null=False,blank=False)
    descricao = TextField(max_length=250,null=False,blank=False)
    conta = models.ForeignKey(Conta,on_delete=models.CASCADE,related_name="receitas")
    TIPORECEITA = (("salario","salario"),("presente","presente"),("premio","premio"),("outros","outros")) 
    tipoReceita = models.CharField(max_length=8,choices=TIPORECEITA)

    def Meta():
        verbose_name = "receita"          # Definindo um tratamento básico para a palavra "receita"
        verbose_name_plural = "receitas"  #   django ira modificar automaticamente quando haver mais de uma receita;

    def get_absolute_url(self):
        return reverse("receita:receita_detail",args=[self.id]) # essa função irá auxilar a criar urls, pois pretendo mostrar os detalhes da receita;
    
    def __str__(self):
        return self.tipoReceita #para no banco de dados aparecer com o tipo de receita;
