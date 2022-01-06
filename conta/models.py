"""
Neste arquivo são criados as variaveis do objeto conta; 
também sao definidas os campos da tabela conta, no banco de dados;
"""

from django.db import models
from django.urls import reverse 

# Create your models here.

#criando a classe conta;
class Conta(models.Model):
    numConta = models.CharField(max_length=8,null=False,blank=False)
    saldo = models.DecimalField(max_digits=9,decimal_places=2,null=False,blank=False) # todos os campos recebem null e blanck = True
    TIPOCONTA = (("1","carteira"),("2","corrente"),("3","poupanca")) # pois quero que sejam preenchidos obrigatoriamente;
    tipoConta = models.CharField(max_length=1,choices=TIPOCONTA) # fiz dessa forma para o usuario escolher o tipo de conta;
    instituicaoFinanceira = models.CharField(max_length=200,null=False,blank=False)

    def Meta():
        verbose_name = "conta"          # Definindo um tratamento básico para a palavra "conta"
        verbose_name_plural = "contas"  #   django ira modificar automaticamente quando haver mais de uma conta;

    def get_absolute_url(self):
        return reverse("conta:conta_detail",args=[self.id]) # essa função irá auxilar a criar urls, pois pretendo mostrar os detalhes da conta;
    
    def __str__(self):
        return self.numConta #para no banco de dados aparecer com o numero da conta;