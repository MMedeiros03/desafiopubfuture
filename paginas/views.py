from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class PaginaPrincipal(TemplateView):
    template_name = "base/home.html"
