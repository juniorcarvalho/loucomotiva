from django.shortcuts import render
from .forms import CadastroForm
from .models import Pessoas


def index(request):
    success = False
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            form = CadastroForm()
            success = True
    else:
        form = CadastroForm()
    context = {}
    context['form'] = form
    context['success'] = success
    return render(request, 'index.html', context)
