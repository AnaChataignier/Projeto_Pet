from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from galeria.models import Pet
from django.db.models import Q
from Tutor.models import Tutor
from galeria.forms import PetForms

def index(request):
    pet = Pet.objects.order_by("data_cadastro").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": pet})
    

def imagem(request, foto_id):
    pet = get_object_or_404(Pet, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"cards": pet})

def buscar(request):
    pet = Pet.objects.order_by("data_cadastro").filter(publicada=True)
    

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            pet = pet.filter(Q(nome__icontains=nome_a_buscar) | Q(tutor__nome__icontains=nome_a_buscar))
            

    return render(request, "galeria/buscar.html", {"cards": pet})

def cadastro_pet(request):
    form = PetForms()
    if request.method == 'POST':
        form = PetForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pet cadastrado!')
            return redirect('index')
            
    return render(request, 'galeria/cadastro_pet.html', {'form': form})


def editar_pet(request, foto_id):
    pet = Pet.objects.get(id=foto_id) 
    form = PetForms(instance=pet)
    
    if request.method == 'POST':
        form = PetForms(request.POST, request.FILES, instance = pet)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pet editado com sucesso!')
            return redirect('index')
    
    return render(request, 'galeria/editar_pet.html', {'form': form, 'foto_id':foto_id})


def deletar_pet(request, foto_id):
    pet = Pet.objects.get(id=foto_id)
    pet.delete()
    messages.success(request, 'Deleção feita com sucesso!')
    return redirect('index')


def filtro(request, categoria):
    pet = Pet.objects.order_by('data_cadastro').filter(publicada=True, categoria=categoria)
    return render(request, 'galeria/index.html', {'cards': pet})