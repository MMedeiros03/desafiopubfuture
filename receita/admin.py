from django.contrib import admin
from .models import Receita
# Register your models here.

"""
No arquivo admin.py é feito o registro do modelo na tela de administração propria do django. 
"""

admin.site.register(Receita)