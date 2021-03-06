"""
Neste arquivo são criados as variaveis do objeto despesa; 
também sao definidas os campos da tabela despesa, no banco de dados;
"""

from typing import ClassVar
from django.db import models
from django.urls import reverse 
from conta.models import Conta

# Create your models here.

TIPODESPESA = [
    ("alimentacao","alimentacao"),
    ("educacao","educacao"),
    ("lazer","lazer"),
    ("moradia","moradia"),
    ("roupa","roupa"),
    ("saude","saude"),
    ("transporte","transporte"),
    ("outros","outros")
]


#criando a classe conta;
class Despesa(models.Model):
    valor = models.CharField(max_length=8,null=False,blank=False)
    dataPagamento = models.DateField(null=False,blank=False) # todos os campos recebem null e blanck = True
    dataPagamentoEsperado = models.DateField(null=False,blank=False) # pois quero que sejam preenchidos obrigatoriamente; 
    tipoDespesa = models.CharField(max_length=11,choices=TIPODESPESA) # fiz dessa forma para o usuario escolher o tipo de despesa;
    conta = models.ForeignKey(Conta,on_delete=models.CASCADE,related_name="despesas") # o campo conta sendo chave estrangeira, ligando as despesas a uma conta;
                                                                                    # ainda utiliza o metodo cascade. Signfica que quando uma conta for excluida,
                                                                                    # as despesas ligadas a ela também serão excluidas;

    def Meta():
        verbose_name = "despesa"          # Definindo um tratamento básico para a palavra "conta"
        verbose_name_plural = "despesas"  #   django ira modificar automaticamente quando haver mais de uma conta;

    def get_absolute_url(self):
        return reverse("paginas:detalhes_despesa",args=[self.id]) # essa função irá auxilar a criar urls, pois pretendo mostrar os detalhes da conta;
    
    def __str__(self):
        return self.tipoDespesa #para no banco de dados aparecer com o numero da conta;