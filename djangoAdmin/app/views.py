from django.shortcuts import render
from .models import *

def listar_veiculo(request, template_name="veiculo_list.html"):
    veiculo = Veiculo.objects.all()
    veiculos = {'lista': veiculo}
    return render(request, template_name, veiculos)
