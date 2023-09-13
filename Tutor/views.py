from django.shortcuts import render, HttpResponse, redirect
from Tutor.forms import CadastroForms
from Tutor.models import Tutor
from django.contrib import messages

def cadastro_tutor(request):
    form = CadastroForms()
    if request.method == 'POST':
        form = CadastroForms(request.POST)
        if form.is_valid():
            email=form['email'].value()
            if Tutor.objects.filter(email=email).exists():
                messages.error(request, "Tutor já cadastrado.")
            form.save()
            return redirect('index')
           
    return render(request, 'Tutor/cadastro_tutor.html', {'form': form})
    

