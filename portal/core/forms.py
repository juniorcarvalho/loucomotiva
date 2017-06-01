from django import forms
from .models import Pessoas
from django.utils.translation import ugettext_lazy as _


class CadastroForm(forms.ModelForm):
    class Meta:
        model = Pessoas
        fields = ['nome', 'email', 'celular', 'whatsapp']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Digite seu nome', "maxlength": "100"}),
            'email': forms.TextInput(attrs={'placeholder': 'Digite seu email', "maxlength": "255"}),
            'celular': forms.TextInput(attrs={'placeholder': 'Digite seu telefone', "maxlength": "13"}),
            'whatsapp': forms.CheckboxInput(attrs={'checked': 'True'}),
        }

        labels = {
            'whatsapp': _('Receber novidades por WhatsApp'),
        }

    def clean_celular(self):
        celular = self.cleaned_data['celular']
        celular = celular.replace("-", "")
        return celular

    def clean_email(self):
        email = self.cleaned_data['email']
        querySet = Pessoas.objects.filter(email=email)
        if querySet.exists():
            raise forms.ValidationError('Email já cadastrado.')
        return email

    def clean_nome(self):
        name = self.cleaned_data['nome']
        words = [w.capitalize() for w in name.split()]
        return ' '.join(words)
