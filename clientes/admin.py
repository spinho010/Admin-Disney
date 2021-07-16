from django.contrib import admin
from clientes.models import Tela, Serviço, Status, Clientes, Tipo

# Register your models here.

class Ver_Tela(admin.ModelAdmin):
    list_display = ('tela_atual', 'observacao1')

admin.site.register(Tela, Ver_Tela)


class Ver_Serviço(admin.ModelAdmin):
    list_display = ('serviço_atual', 'observacao2')

admin.site.register(Serviço, Ver_Serviço)


class Ver_Status(admin.ModelAdmin):
    list_display = ('status_atual', 'observacao3')

admin.site.register(Status, Ver_Status)


class Ver_Clientes(admin.ModelAdmin):
    list_display = ('nome', 'plano', 'proximo_pagamento', 'ultimo_pagamento')

admin.site.register(Clientes, Ver_Clientes)


class Ver_Tipo(admin.ModelAdmin):
    list_display = ('tipo_atual', 'observacao4')

admin.site.register(Tipo, Ver_Tipo)