from django.shortcuts import render, get_object_or_404, redirect

from galeria.models import Fotografia
from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado!")
        return redirect('login')
        
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def busca(request):
    if not request.usar.is_authenticated:
        messages.error(request, "Usuário não logado!")
        return redirect('login')

    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    if "busca" in request.GET:
        nome_a_busca = request.GET['busca']
        if nome_a_busca:
            fotografias = fotografias.filter(nome__icontains=nome_a_busca)

    return render(request, "galeria/busca.html", {"cards": fotografias})