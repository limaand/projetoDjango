from django.shortcuts import render
from .models import *

#def listar_veiculo(request, template_name="veiculo_list.html"):
#    veiculo = Veiculo.objects.all()
#    veiculos = {'lista': veiculo}
#    return render(request, template_name, veiculos)


def listar_veiculo(request, template_name="veiculo_list.html"):
    query = request.GET.get("busca", '')
    ordenar = request.GET.get("ordernar", '')
    if query:
        veiculo = Veiculo.objects.filter(modelo__icontains=query)
    else:
        if ordenar:
            veiculo = Veiculo.objects.all().order_by(ordenar)
        else:
            veiculo = Veiculo.objects.all()

    veiculo = {'lista':veiculo}
    return render(request, template_name, veiculo)