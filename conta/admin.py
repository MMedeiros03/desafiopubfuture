from django.contrib import admin
from .models import Conta
# Register your models here.

"""
No arquivo admin.py é feito o registro do modelo na tela de administração propria do django. 
"""

admin.site.register(Conta)