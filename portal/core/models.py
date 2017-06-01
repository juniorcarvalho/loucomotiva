from django.db import models


class Pessoas(models.Model):
    nome = models.CharField('nome', max_length=100)
    email = models.EmailField('Email', unique=True)
    celular = models.CharField('Telefone', max_length=13)
    whatsapp = models.BooleanField('Whatsapp')
    email_ok = models.BooleanField('Email confirmado', default=False)
    email_marketing = models.BooleanField('Email Marketing', default=False)
    cadastro = models.DateTimeField('Criado em', auto_now_add=True)
    alterado = models.DateTimeField('Modificado em', auto_now=True)

