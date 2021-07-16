from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class Tela(models.Model):
    tela_atual = models.CharField(max_length=60)
    observacao1 = models.CharField(verbose_name='Observação:', max_length=60, blank=True)

    def __str__(self):
            return "{}".format(self.tela_atual)


class Serviço(models.Model):
    serviço_atual = models.CharField(max_length=60)
    observacao2 = models.CharField(verbose_name='Observação:', max_length=60, blank=True)

    def __str__(self):
            return "{}".format(self.serviço_atual)

class Status(models.Model):
    status_atual = models.CharField(verbose_name='Status:', max_length=60, blank=True)
    observacao3 = models.CharField(verbose_name='Observação:', max_length=60, blank=True)

    def __str__(self):
            return "{}".format(self.status_atual)


class Tipo(models.Model):
    tipo_atual = models.CharField(verbose_name='Serviço:', max_length=60, blank=True)
    observacao4 = models.CharField(verbose_name='Observação:', max_length=60, blank=True)

    def __str__(self):
            return "{}".format(self.tipo_atual)



class Clientes(models.Model):
    nome = models.CharField(verbose_name='Nome:', max_length=60, blank=True)
    plano = models.ForeignKey(Serviço, max_length=60, null=True, on_delete=models.PROTECT)
    tela_agora = models.ForeignKey(Tela, max_length=60, null=True, on_delete=models.PROTECT)
    status_agora = models.ForeignKey(Status, max_length=60, null=True, on_delete=models.PROTECT)
    proximo_pagamento = models.DateTimeField(max_length=90, null=True)
    ultimo_pagamento = models.DateTimeField(max_length=90, null=True)
    serviço_atualmente = models.ForeignKey(Tipo, max_length=60, null=True, on_delete=models.PROTECT)

    def __str__(self):
            return "{}".format(self.nome)