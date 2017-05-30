# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-30 02:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('celular', models.CharField(max_length=11, verbose_name='Telefone')),
                ('whatsapp', models.BooleanField(verbose_name='Whatsapp')),
                ('email_ok', models.BooleanField(verbose_name='Email confirmado')),
                ('email_marketing', models.BooleanField(verbose_name='Email Marketing')),
            ],
        ),
    ]
