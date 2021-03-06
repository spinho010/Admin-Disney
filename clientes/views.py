from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
import io
from django.template.loader import get_template
from django.urls import reverse_lazy
from clientes.models import Clientes

class Home(ListView):
    model = Clientes
    template_name = 'home.html'


class Fichas(ListView):
    model = Clientes
    template_name = 'fichas.html'


class Conta(TemplateView):
    template_name = 'conta.html'


class vender(TemplateView):
    template_name = 'vendas.html'


class sucess(TemplateView):
    template_name = 'sucess.html'


class process(TemplateView):
    template_name = 'process.html'



class UpdateFichas(UpdateView):
    model = Clientes
    fields = ['status_agora', 'proximo_pagamento', 'ultimo_pagamento']
    template_name = 'atualizar.html'
    success_url = ('/')


class CreateClientes(CreateView):
    model = Clientes
    fields = ['nome', 'plano', 'tela_agora','status_agora', 'proximo_pagamento', 'ultimo_pagamento', 'serviço_atualmente']
    template_name = 'novo_cliente.html'
    success_url = ('/')