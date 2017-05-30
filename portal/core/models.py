from django.db import models


class Pessoas(models.Model):
    nome = models.CharField('nome', max_length=100)
    email = models.EmailField('Email')
    celular = models.CharField('Telefone', max_length=11)
    whatsapp = models.BooleanField('Whatsapp')
    email_ok = models.BooleanField('Email confirmado')
    email_marketing = models.BooleanField('Email Marketing')
